# parla

Un proyecto de piruetas, 2026.

## Módulos

Cada módulo tiene su propia carpeta con un proyecto de KiCad, organizado por versión y revisión (por ejemplo `parla-linea/parla-linea-v-0-rev-a/`).

|                      | parla-linea                            | parla-eurorack                           | parla-guitarra        | parla-estereo          |
| -------------------- | -------------------------------------- | ---------------------------------------- | --------------------- | ---------------------- |
| formato              | standalone                             | eurorack                                 | standalone            | standalone             |
| entrada alimentación | batería 9V                             | por definir                              | batería 9V            | por definir            |
| chip                 | PAM8403                                | por definir                              | LM386                 | PAM8403                |
| interfaz             | 1x pote                                | 2x potes                                 | 1x pote               | 2x potes               |
| entrada señal        | 1x línea TRS                           | 1x eurorack                              | 1x guitarra           | 1x línea TRS           |
| conector entrada     | TRS 1/8"                               | TS 1/8"                                  | TS 1/4"               | TRS 1/8"               |
| salidas              | 1x parlante, 1x línea                  | 1x parlante, 1x eurorack                 | 1x parlante           | 2x parlantes           |
| conector salida      | parlante: por definir, línea: TRS 1/8" | parlante: por definir, eurorack: TS 1/8" | parlante: por definir | parlantes: por definir |

### Extensores

|                  | parla-linea-extensor  | parla-eurorack-extensor |
| ---------------- | --------------------- | ----------------------- |
| formato          | standalone            | eurorack                |
| alimentación     | ninguna               | por definir             |
| chip             | ninguno               | por definir             |
| interfaz         | —                     | —                       |
| entradas         | 1x línea              | 1x eurorack             |
| conector entrada | TRS 1/8"              | TS 1/8"                 |
| salidas          | 1x parlante           | 1x parlante             |
| conector salida  | parlante: por definir | parlante: por definir   |

## Documentación

Esquemáticos, placas y bill of materials (BOM) de cada módulo, generados automáticamente: [docs](./docs/README.md).

### Agregar las bibliotecas de parla-linea a KiCad

Las bibliotecas generadas están en `parla-linea/parla-linea-v-0-rev-a/bibliotecas/`.
Para que KiCad las encuentre, abre primero el proyecto
`parla-linea/parla-linea-v-0-rev-a/parla-linea-v-0-rev-a.kicad_pro` y agrégalas
como bibliotecas específicas de ese proyecto:

1. En KiCad, abre **Preferencias → Administrar bibliotecas de símbolos…**.
2. En **Bibliotecas específicas del proyecto**, pulsa **Añadir biblioteca existente**
   y selecciona
   `parla-linea/parla-linea-v-0-rev-a/bibliotecas/parla-linea-v-0-rev-a.kicad_sym`.
3. Abre **Preferencias → Administrar bibliotecas de huellas…**.
4. En **Bibliotecas específicas del proyecto**, pulsa **Añadir biblioteca existente**
   y selecciona la carpeta
   `parla-linea/parla-linea-v-0-rev-a/bibliotecas/parla-linea-v-0-rev-a.pretty`
   (no un archivo dentro de ella).
5. Confirma los cambios. Las bibliotecas deberían aparecer en los selectores de
   símbolos y huellas del proyecto.

Agrégalas como bibliotecas **específicas del proyecto**, no globales, para que las
rutas queden asociadas a este proyecto. Los modelos 3D están en la carpeta hermana
`parla-linea/parla-linea-v-0-rev-a/bibliotecas/parla-linea-v-0-rev-a.3dshapes/`;
las huellas los referencian desde ahí, así que no hace falta registrarlos como
biblioteca aparte. Si el proyecto ya estaba abierto mientras agregabas las
bibliotecas, cierra y vuelve a abrir el proyecto.

### Enlaces por módulo

- parla-linea: [carpeta](https://github.com/piruetasxyz/parla/tree/main/parla-linea), [docs](./docs/parla-linea.md)
- parla-eurorack: [carpeta](https://github.com/piruetasxyz/parla/tree/main/parla-eurorack), [docs](./docs/parla-eurorack.md)
- parla-guitarra: [carpeta](https://github.com/piruetasxyz/parla/tree/main/parla-guitarra), [docs](./docs/parla-guitarra.md)
- parla-estereo: [carpeta](https://github.com/piruetasxyz/parla/tree/main/parla-estereo), [docs](./docs/parla-estereo.md)
- parla-linea-extensor: [carpeta](https://github.com/piruetasxyz/parla/tree/main/parla-linea-extensor), [docs](./docs/parla-linea-extensor.md)
- parla-eurorack-extensor: [carpeta](https://github.com/piruetasxyz/parla/tree/main/parla-eurorack-extensor), [docs](./docs/parla-eurorack-extensor.md)

## Versiones antiguas

Hicimos versiones preliminares que están en la carpeta [versiones-antiguas](https://github.com/piruetasxyz/parla/tree/main/versiones-antiguas):

- `parla-v0-borrador`: primeros experimentos de esquemáticos (enero-febrero 2026).
- `parla-v0-revA`: versión producida con SMD en JLCPCB.
- `parla-v0-revB`: revisión de la placa con algunos cambios (junio 2026), junto a sus gerbers y archivos de PCBA.
- `graficas`: logos y gráficas usadas en las placas.
