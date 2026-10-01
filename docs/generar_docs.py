#!/usr/bin/env python3
"""Regenera la documentación de cada módulo en docs/:

- docs/images/<modulo>-esquematico.svg y docs/images/<modulo>-placa.svg
- la tabla "Bill of materials" en docs/<modulo>.md (entre las marcas
  BOM_TABLE_START y BOM_TABLE_END)

Los módulos se descubren solos: cada carpeta parla-*/ en la raíz del repo es
un módulo, y su revisión activa es la subcarpeta <modulo>-v-N-rev-X más
reciente. Si un módulo todavía no tiene docs/<modulo>.md, se crea con una
plantilla. Así, al agregar un módulo o una revisión nueva no hay que tocar ni
este script ni .github/workflows/actualizar-capturas.yml.

Uso: python3 docs/generar_docs.py
Requiere kicad-cli (KiCad 10) en el PATH, o la variable de entorno KICAD_CLI
con el comando completo (por ejemplo, envuelto en "docker run ... kicad-cli"
como en .github/workflows/actualizar-capturas.yml).
"""
import csv
import os
import re
import shlex
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS = REPO_ROOT / "docs"
IMAGENES = DOCS / "images"

# lib_id ("Biblioteca:Nombre") -> descripción en español, para la columna
# Descripción de la tabla. Si aparece un lib_id que no está acá, el script
# avisa por stderr y usa el lib_id tal cual como descripción de respaldo.
DESCRIPCIONES = {
    "Device:R": "Resistencia",
    "Device:R_Potentiometer": "Potenciómetro",
    "Device:C": "Capacitor cerámico",
    "Device:C_Polarized": "Capacitor electrolítico",
    "Device:D_Schottky": "Diodo Schottky",
    "Device:Speaker": "Parlante",
    "Amplifier_Audio:LM386": "Amplificador de audio LM386",
    "Amplifier_Audio:PAM8403D": "Amplificador de audio clase D",
    "Connector_Audio:AudioJack2_SwitchT": "Jack de audio mono",
    "Connector_Audio:AudioJack3_SwitchT": "Jack de audio estéreo",
    "Connector:Screw_Terminal_01x02": "Bornera de 2 pines",
    "Connector_Generic:Conn_02x05_Odd_Even": "Header de alimentación Eurorack (10 pines)",
    "Regulator_Linear:L7805": "Regulador de voltaje lineal +5V",
}

INICIO_MARCA = "<!-- BOM_TABLE_START -->"
FIN_MARCA = "<!-- BOM_TABLE_END -->"

KICAD_CLI = shlex.split(os.environ.get("KICAD_CLI", "kicad-cli"))

PATRON_REVISION = re.compile(r"-v-(\d+)-rev-([a-z]+)$")


def descubrir_modulos() -> list[tuple[str, str, Path]]:
    """Devuelve (modulo, revision, carpeta relativa a REPO_ROOT) por módulo."""
    modulos = []
    for carpeta_modulo in sorted(REPO_ROOT.glob("parla-*")):
        if not carpeta_modulo.is_dir():
            continue
        modulo = carpeta_modulo.name
        revisiones = []
        for carpeta in carpeta_modulo.iterdir():
            m = PATRON_REVISION.search(carpeta.name)
            if carpeta.is_dir() and carpeta.name.startswith(modulo + "-") and m:
                # orden por versión numérica y después por letra de revisión
                # (rev-z < rev-aa), para que v-10 quede después de v-2
                clave = (int(m.group(1)), len(m.group(2)), m.group(2))
                revisiones.append((clave, carpeta))
        if not revisiones:
            print(f"[aviso] {modulo} no tiene carpetas de revisión, se omite", file=sys.stderr)
            continue
        _, carpeta = max(revisiones)
        revision = carpeta.name[len(modulo) + 1:]
        modulos.append((modulo, revision, carpeta.relative_to(REPO_ROOT)))
    return modulos


def kicad(*args: str) -> None:
    # Rutas siempre relativas a REPO_ROOT: cuando KICAD_CLI envuelve un
    # "docker run" (como en CI), el contenedor solo tiene montado REPO_ROOT
    # como /work, así que no sirven rutas absolutas del host.
    resultado = subprocess.run(
        [*KICAD_CLI, *args], capture_output=True, text=True, cwd=REPO_ROOT
    )
    if resultado.returncode != 0:
        print(resultado.stdout, resultado.stderr, sep="\n", file=sys.stderr)
        resultado.check_returncode()


def generar_esquematico(modulo: str, sch_rel: str) -> None:
    # "sch export svg" recibe una carpeta y escribe un SVG por hoja; nos
    # quedamos con la hoja raíz, que se llama igual que el .kicad_sch.
    tmp_rel = f"_captura_tmp/{modulo}"
    tmp = REPO_ROOT / tmp_rel
    shutil.rmtree(tmp, ignore_errors=True)
    tmp.mkdir(parents=True)
    try:
        kicad("sch", "export", "svg", "--output", tmp_rel, sch_rel)
        raiz = tmp / (Path(sch_rel).stem + ".svg")
        svg = raiz if raiz.exists() else next(tmp.glob("*.svg"), None)
        if svg is None:
            sys.exit(f"[error] no se generó SVG del esquemático para {modulo}")
        shutil.move(svg, IMAGENES / f"{modulo}-esquematico.svg")
    finally:
        shutil.rmtree(REPO_ROOT / "_captura_tmp", ignore_errors=True)


def generar_placa(modulo: str, pcb_rel: str) -> None:
    kicad(
        "pcb", "export", "svg",
        "--layers", "F.Cu,F.Mask,F.Silkscreen,Edge.Cuts",
        "--mode-single",
        "--output", f"docs/images/{modulo}-placa.svg",
        pcb_rel,
    )


def exportar_bom(sch_rel: str) -> list[dict]:
    # kicad-cli no soporta escribir a stdout: "--output -" crea un archivo
    # literal llamado "-". Hay que darle un archivo real, relativo a REPO_ROOT.
    tmp_nombre = f"_bom_tmp_{Path(sch_rel).stem}.csv"
    tmp_path = REPO_ROOT / tmp_nombre
    try:
        kicad(
            "sch", "export", "bom",
            "--output", tmp_nombre,
            "--fields", "Reference,Value,Footprint,QUANTITY,${SYMBOL_LIBRARY},${SYMBOL_NAME}",
            "--labels", "Refs,Value,Footprint,Qty,Lib,Name",
            "--group-by", "Value,Footprint",
            "--ref-range-delimiter", "",
            "--ref-delimiter", ", ",
            sch_rel,
        )
        with open(tmp_path, newline="") as f:
            return list(csv.DictReader(f))
    finally:
        tmp_path.unlink(missing_ok=True)


def generar_tabla(filas: list[dict]) -> str:
    if not filas:
        return "*(el esquemático todavía no tiene componentes)*"
    lineas = [
        "| Referencias | Cantidad | Valor | Huella | Descripción |",
        "| --- | --- | --- | --- | --- |",
    ]
    total = 0
    for fila in filas:
        lib_id = f"{fila['Lib']}:{fila['Name']}"
        descripcion = DESCRIPCIONES.get(lib_id)
        if descripcion is None:
            print(f"[aviso] sin descripción para '{lib_id}', agregar a DESCRIPCIONES en generar_docs.py", file=sys.stderr)
            descripcion = lib_id
        valor = fila["Value"] or "*(valor sin definir)*"
        huella = fila["Footprint"] or "*(sin huella asignada)*"
        total += int(fila["Qty"])
        lineas.append(f"| {fila['Refs']} | {fila['Qty']} | {valor} | {huella} | {descripcion} |")
    lineas.append("")
    faltan_valor = any(f["Value"] == "" for f in filas)
    faltan_huella = any(f["Footprint"] == "" for f in filas)
    if faltan_valor or faltan_huella:
        lineas.append(
            f"{total} componentes en total. Los ítems marcados "
            + ("*(valor sin definir)*" if faltan_valor else "")
            + (" y " if faltan_valor and faltan_huella else "")
            + ("*(sin huella asignada)*" if faltan_huella else "")
            + " todavía no están completos en el esquemático — hay que completarlos antes de generar gerbers o comprar partes para esta revisión."
        )
    else:
        lineas.append(f"{total} componentes en total.")
    return "\n".join(lineas)


def plantilla_doc(modulo: str, revision: str, carpeta: Path) -> str:
    base = f"{carpeta}/{carpeta.name}"
    return f"""# {modulo}

[volver al índice](./README.md)

## Revisión activa

`{revision}`

## Esquemático y placa

Generados automáticamente por GitHub Actions a partir de `{base}.kicad_sch` y `.kicad_pcb` en cada push que los modifica.

![Esquemático de {modulo} {revision}](./images/{modulo}-esquematico.svg)

![Placa de {modulo} {revision}](./images/{modulo}-placa.svg)

## Bill of materials

Generado a partir de `{base}.kicad_sch`.

{INICIO_MARCA}
{FIN_MARCA}
"""


def actualizar_doc(modulo: str, revision: str, carpeta: Path, tabla: str) -> None:
    doc_path = DOCS / f"{modulo}.md"
    if not doc_path.exists():
        doc_path.write_text(plantilla_doc(modulo, revision, carpeta))
        print(f"creado: {doc_path}")
    texto = doc_path.read_text()
    patron = re.compile(re.escape(INICIO_MARCA) + r".*?" + re.escape(FIN_MARCA), re.S)
    reemplazo = f"{INICIO_MARCA}\n{tabla}\n{FIN_MARCA}"
    nuevo_texto, n = patron.subn(lambda _: reemplazo, texto)
    if n == 0:
        sys.exit(f"[error] no se encontraron las marcas {INICIO_MARCA}/{FIN_MARCA} en {doc_path}")
    if nuevo_texto != texto:
        doc_path.write_text(nuevo_texto)
        print(f"actualizado: {doc_path}")
    else:
        print(f"sin cambios: {doc_path}")


def main() -> None:
    IMAGENES.mkdir(parents=True, exist_ok=True)
    for modulo, revision, carpeta in descubrir_modulos():
        base = f"{carpeta}/{carpeta.name}"
        print(f"== {modulo} ({revision})")
        generar_esquematico(modulo, f"{base}.kicad_sch")
        generar_placa(modulo, f"{base}.kicad_pcb")
        actualizar_doc(modulo, revision, carpeta, generar_tabla(exportar_bom(f"{base}.kicad_sch")))


if __name__ == "__main__":
    main()
