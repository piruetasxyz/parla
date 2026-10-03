# parla-linea

[volver al índice](./README.md)

## Especificaciones

- formato: standalone
- interfaz: 2x potes
- entradas: 1x TRS 1/8"
- salidas: 1x parlante, 1x TRS 1/8"

## Revisión activa

`v-0-rev-a`

## Esquemático y placa

Generados automáticamente por GitHub Actions a partir de `parla-linea/parla-linea-v-0-rev-a/parla-linea-v-0-rev-a.kicad_sch` y `.kicad_pcb` en cada push que los modifica.

![Esquemático de parla-linea v-0-rev-a](./images/parla-linea-esquematico.svg)

![Placa de parla-linea v-0-rev-a](./images/parla-linea-placa.svg)

## Bill of materials

Generado a partir de `parla-linea/parla-linea-v-0-rev-a/parla-linea-v-0-rev-a.kicad_sch`.

<!-- BOM_TABLE_START -->
| Referencias | Cantidad | Valor | Huella | Descripción |
| --- | --- | --- | --- | --- |
| C1, C6 | 2 | C | *(sin huella asignada)* | Capacitor cerámico |
| C2, C7 | 2 | 100n | *(sin huella asignada)* | Capacitor cerámico |
| C3 | 1 | 100u | *(sin huella asignada)* | Capacitor electrolítico |
| C4 | 1 | 10u | *(sin huella asignada)* | Capacitor electrolítico |
| D1 | 1 | 1N4007 | *(sin huella asignada)* | Device:D |
| D2 | 1 | LED | Eurocad:LED3mm | Device:LED |
| J2, J4 | 2 | AudioJack2_SwitchT | Connector_Audio:Jack_3.5mm_QingPu_WQP-PJ398SM_Vertical_CircularHoles | Jack de audio mono |
| J3, J5 | 2 | Screw_Terminal_01x02 | TerminalBlock:TerminalBlock_MaiXu_MX126-5.0-02P_1x02_P5.00mm | Bornera de 2 pines |
| J6 | 1 | AudioJack3_SwitchTR | Connector_Audio:Jack_3.5mm_CUI_SJ1-3525N_Horizontal | Connector_Audio:AudioJack3_SwitchTR |
| J7 | 1 | Conn_01x03_Pin | Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical | Connector:Conn_01x03_Pin |
| R1, R2 | 2 | 10k | *(sin huella asignada)* | Resistencia |
| R3 | 1 | 1k | *(sin huella asignada)* | Resistencia |
| RV1 | 1 | 100kB | Potentiometer_THT:Potentiometer_Alps_RK163_Dual_Horizontal | Device:R_Potentiometer_Dual_Separate |
| U1 | 1 | PAM8403D | Package_SO:SOIC-16_3.9x9.9mm_P1.27mm | Amplificador de audio clase D |
| U2 | 1 | L7805 | *(sin huella asignada)* | Regulador de voltaje lineal +5V |

20 componentes en total. Los ítems marcados *(sin huella asignada)* todavía no están completos en el esquemático — hay que completarlos antes de generar gerbers o comprar partes para esta revisión.
<!-- BOM_TABLE_END -->
