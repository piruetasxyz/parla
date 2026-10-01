# parla

Un proyecto de piruetas, 2026.

## Módulos

Cada módulo tiene su propia carpeta con un proyecto de KiCad, organizado por versión y revisión (por ejemplo `parla-linea/parla-linea-v-0-rev-a/`).

### Principales

| módulo | formato | interfaz | entradas | salidas | docs |
| --- | --- | --- | --- | --- | --- |
| [parla-linea](https://github.com/piruetasxyz/parla/tree/main/parla-linea) | standalone | 2x potes | 1x TRS 1/8" | 1x parlante, 1x TRS 1/8" | [docs](./docs/parla-linea.md) |
| [parla-linea-extensor](https://github.com/piruetasxyz/parla/tree/main/parla-linea-extensor) | standalone | — | 1x TRS 1/8" | 1x parlante | [docs](./docs/parla-linea-extensor.md) |
| [parla-eurorack](https://github.com/piruetasxyz/parla/tree/main/parla-eurorack) | eurorack | 2x potes | 1x TS 1/8" | 1x parlante, 1x TS 1/8" | [docs](./docs/parla-eurorack.md) |
| [parla-eurorack-extensor](https://github.com/piruetasxyz/parla/tree/main/parla-eurorack-extensor) | eurorack | — | 1x TS 1/8" | 1x parlante | [docs](./docs/parla-eurorack-extensor.md) |

### Otros

| módulo | formato | interfaz | entradas | salidas | docs |
| --- | --- | --- | --- | --- | --- |
| [parla-guitarra](https://github.com/piruetasxyz/parla/tree/main/parla-guitarra) | standalone | 1x pote | 1x TS 1/4" | 1x parlante | [docs](./docs/parla-guitarra.md) |
| [parla-estereo](https://github.com/piruetasxyz/parla/tree/main/parla-estereo) | standalone | 2x potes | 1x TRS 1/8" | 2x parlantes | [docs](./docs/parla-estereo.md) |

## Documentación

Esquemáticos, placas y bill of materials (BOM) de cada módulo, generados automáticamente: [docs](./docs/README.md).

## Versiones antiguas

Hicimos versiones preliminares que están en la carpeta [versiones-antiguas](https://github.com/piruetasxyz/parla/tree/main/versiones-antiguas):

- `parla-v0-borrador`: primeros experimentos de esquemáticos (enero-febrero 2026).
- `parla-v0-revA`: versión producida con SMD en JLCPCB.
- `parla-v0-revB`: revisión de la placa con algunos cambios (junio 2026), junto a sus gerbers y archivos de PCBA.
- `graficas`: logos y gráficas usadas en las placas.
