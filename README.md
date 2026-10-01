# parla

Un proyecto de piruetas, 2026.

## Módulos

Cada módulo tiene su propia carpeta con un proyecto de KiCad, organizado por versión y revisión (por ejemplo `parla-linea/parla-linea-v-0-rev-a/`).

|                      | parla-linea                            | parla-eurorack                           | parla-guitarra        | parla-estereo          |
| -------------------- | -------------------------------------- | ---------------------------------------- | --------------------- | ---------------------- |
| **formato**          | standalone                             | eurorack                                 | standalone            | standalone             |
| **alimentación**     | por definir                            | por definir                              | 9V (bornera)          | por definir            |
| **chip**             | por definir                            | por definir                              | LM386                 | por definir            |
| **interfaz**         | 2x potes                               | 2x potes                                 | 1x pote               | 2x potes               |
| **entradas**         | 1x línea                               | 1x eurorack                              | 1x guitarra           | 1x línea estéreo       |
| **conector entrada** | TRS 1/8"                               | TS 1/8"                                  | TS 1/4"               | TRS 1/8"               |
| **salidas**          | 1x parlante, 1x línea                  | 1x parlante, 1x eurorack                 | 1x parlante           | 2x parlantes           |
| **conector salida**  | parlante: por definir, línea: TRS 1/8" | parlante: por definir, eurorack: TS 1/8" | parlante: por definir | parlantes: por definir |

### Extensores

|                      | parla-linea-extensor  | parla-eurorack-extensor |
| -------------------- | --------------------- | ----------------------- |
| **formato**          | standalone            | eurorack                |
| **alimentación**     | por definir           | por definir             |
| **chip**             | por definir           | por definir             |
| **interfaz**         | —                     | —                       |
| **entradas**         | 1x línea              | 1x eurorack             |
| **conector entrada** | TRS 1/8"              | TS 1/8"                 |
| **salidas**          | 1x parlante           | 1x parlante             |
| **conector salida**  | parlante: por definir | parlante: por definir   |

## Documentación

Esquemáticos, placas y bill of materials (BOM) de cada módulo, generados automáticamente: [docs](./docs/README.md).

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
