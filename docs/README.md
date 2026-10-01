# docs

Documentación por módulo: esquemático, placa y lista de materiales bill of materials (BOM) de la revisión activa de cada uno.

- [parla-linea](./parla-linea.md)
- [parla-linea-extensor](./parla-linea-extensor.md)
- [parla-eurorack](./parla-eurorack.md)
- [parla-eurorack-extensor](./parla-eurorack-extensor.md)
- [parla-guitarra](./parla-guitarra.md)
- [parla-estereo](./parla-estereo.md)

Las capturas SVG y las tablas BOM las genera [generar_docs.py](./generar_docs.py), que corre automáticamente en GitHub Actions (`.github/workflows/actualizar-capturas.yml`) en cada push a `main` que modifica un `.kicad_sch` o `.kicad_pcb`. La revisión activa de cada módulo es la carpeta `<modulo>-v-N-rev-X` más reciente dentro de `parla-*/`, así que al agregar una revisión o un módulo nuevo no hay que editar nada: el script lo detecta y, si el módulo es nuevo, crea su página acá (falta agregarla a mano a esta lista).

Para correrlo localmente (requiere `kicad-cli` de KiCad 10):

```sh
python3 docs/generar_docs.py
```
