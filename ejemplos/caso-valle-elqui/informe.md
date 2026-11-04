# Verificación de SLA de Agrícola Valle de Elqui SpA

## 1 Identificación

| Campo | Identificación |
| --- | --- |
| Servicio | Internet dedicado simétrico de 200 Mbps |
| Cliente y ubicación | Agrícola Valle de Elqui SpA, planta Vicuña |
| Proveedor | NorteNet Telecomunicaciones |
| Período contractual | 1 al 30 de septiembre de 2026; 30 días; 43.200 minutos |
| Demarcación | Puerto LAN del CPE instalado en la planta Vicuña |
| Destinatario | Gerencia de Operaciones |
| Integrantes | Jose Alberto Tapia Cerda |
| Control del documento | Versión 1.1 del informe; emisión 4 de noviembre de 2026 |

## 2 Resumen ejecutivo

El SLA de septiembre no se cumple: disponibilidad de 99,62963% y respuesta de 66 minutos en INC-2672.
Latencia, jitter y throughput cumplen; la pérdida mensual tiene evidencia insuficiente.
La restauración cumple el límite de cuatro horas por incidente atribuible.
Corresponde un crédito de 15%, equivalente a $180.000 neto sobre el cargo de $1.200.000.

## 3 Alcance y referencias

Se evalúan las cláusulas 2.1, 2.2, 3.1 a 3.5, 4.1, 4.2, 5.1, 6.1, 6.2, 7.2 y 8.1 a 8.4 del extracto contractual [F1, p. 2]. El análisis cubre el acceso de Internet que soporta el ERP, la trazabilidad de exportación y la telefonía IP de la planta.

La evidencia contractual termina en el puerto LAN del CPE. Las pruebas PE-core no representan ese trayecto y el resultado de un notebook por Wi-Fi incorpora factores ajenos al punto de medición pactado. El crédito se determina por las cláusulas del SLA, no por la percepción de calidad ni por un máximo observado aislado.

### 3 1 Matriz de compromisos contractuales

| Cláusula y métrica | Objetivo y período | Punto y método | Estadístico |
| --- | --- | --- | --- |
| 3.1 Disponibilidad | ≥99,9% mensual | Servicio en demarcación; NMS y tickets | Minutos atribuibles sobre 43.200 min |
| 3.2 Latencia | ≤30 ms; mes calendario | CPE a servidor del proveedor en La Serena; ICMP cada 60 s | RTT promedio mensual |
| 3.3 Jitter | ≤10 ms; mes calendario | TWAMP desde demarcación; referencia RFC 3393 | Promedio mensual, ponderado por muestras |
| 3.4 Pérdida | ≤0,5%; mes calendario | TWAMP desde demarcación | Paquetes perdidos / enviados |
| 3.5 Throughput | ≥90% de 200 Mbps = 180 Mbps; ≥4 pruebas/mes | iperf3 TCP en demarcación; marco RFC 6349 | Promedio de las pruebas válidas |
| 4.1 Respuesta | ≤60 min en 100% de incidentes | Apertura a primera respuesta; tickets | Evaluación individual; máximo de control |
| 4.2 MTTR | ≤4 h = 240 min por incidente atribuible | Ticket y restauración NMS | Tiempo de restauración por incidente |
| 5.1 Cobertura | ≥90% del mes | Registros en punto y método pactados | Datos válidos / datos esperados |
| 6.1 y 6.2 Exclusiones | Aviso ≥72 h y ≤4 h/mes; fuerza mayor declarada; causas del cliente | Avisos, diagnósticos y responsabilidades | Tiempo excluido se considera disponible |

### 3 2 Marco técnico aplicado

ITIL 4 Service Level Management se aplica al acuerdo, seguimiento y revisión de niveles de servicio. ISO/IEC 20000-1:2018 orienta la gestión del servicio, la medición y la mejora. ITU-T E.860 aporta la estructura del SLA y la delimitación de responsabilidades [N1-N3]. No se realiza una auditoría de certificación ISO.

ITU-T Y.1540 define parámetros de transferencia y disponibilidad IP. RFC 3393 describe la variación del retardo; RFC 5357 define TWAMP; RFC 6349 establece un marco de pruebas de throughput TCP [N4-N7]. Los umbrales 30 ms, 10 ms, 0,5% y 90% son contractuales. El uso de iperf3 no acredita, por sí solo, la ejecución completa de todos los procedimientos de RFC 6349.

## 4 Metodología

Se correlacionan eventos NMS, avisos de mantención, diagnósticos y tickets por fecha. Se conservan los minutos reales de interrupción para evaluar disponibilidad; la exclusión modifica la atribución, no la duración del mes. El período se normaliza al denominador de 43.200 minutos fijado en el caso.

### 4 1 Evidencia y cobertura

| Métrica | Fuente y frecuencia | Cobertura y decisión |
| --- | --- | --- |
| Disponibilidad | Anexos 1 y 2; registro de eventos NMS y tickets | Se acepta el registro mensual del caso como completo. No se aporta bitácora cruda para auditar continuidad del NMS. |
| Latencia | Anexo 3; Zabbix ICMP cada 60 s | 42.725 / 43.200 = 98,900463%; supera 90%. Se acepta promedio de 27,4 ms. |
| Jitter | Anexo 4; cuatro bloques TWAMP, último de nueve días | 42.725 muestras entre 1 y 30-sep. Cobertura nominal 98,900463% si la cadencia es 60 s; supuesto por verificar. |
| Pérdida | Anexo 5; TWAMP disponible del 1 al 18-sep | 18 / 30 = 60% de cobertura temporal nominal; inferior a 90%. Evidencia insuficiente. |
| Throughput | Anexo 6; iperf3 TCP, cuatro flujos, 60 s | Cuatro pruebas válidas en CPE. Se aplica la frecuencia específica de 3.5, no muestreo continuo del mes. |
| Respuesta y MTTR | Anexos 1 y 2; cuatro tickets correlacionados | Respuesta: 4/4 tickets. Restauración atribuible: 3/3 incidentes. MNT-0903 es aviso programado. |

### 4 2 Tratamiento de datos y límites

Los cálculos se realizan sin redondeos intermedios; las comparaciones usan el valor no redondeado. La desviación es medido menos objetivo; se expresa en puntos porcentuales (pp) para porcentajes. El 0,31% de pérdida parcial se conserva como observación del 1 al 18-sep; no se extrapola, no se reemplaza por cero y no genera un crédito demostrado.

Se descartan el RTT de 22,1 ms y la pérdida de 0,18% del proveedor por corresponder al trayecto PE-core. Se descarta el Speedtest de 95 Mbps por herramienta, medio y punto distintos de los pactados. Se conserva como señal para diagnóstico interno de la LAN y el Wi-Fi.

El anexo 4 contiene jitter posterior al 19-sep, aunque el anexo 5 informa la detención del colector TWAMP. Para resolver el ejercicio se acepta el anexo 4 como evidencia independiente. Deben verificarse identificadores de sesión, colector, timestamps y cadencia; si proceden del mismo colector detenido y no existen registros alternativos, el jitter pasaría a evidencia insuficiente. Esta salvedad no cambia los dos incumplimientos demostrados ni el crédito calculado.

Se consideran muestras comparables de jitter con el mismo método y configuración. No se equipara variación del RTT con retardo unidireccional. Tampoco se certifican por separado subida y bajada: el anexo de throughput entrega un único resultado por prueba sin identificar la dirección.

## 5 Resultados

### 5 1 Dictamen por métrica

| Métrica | Objetivo | Medido | Desviación | Evidencia | Veredicto |
| --- | --- | --- | --- | --- | --- |
| Disponibilidad | ≥99,9% | 99,629630% | −0,270370 pp | 160 min: E2, E4 y E5; anexos 1-2 | NO CUMPLE |
| Latencia RTT | ≤30 ms | 27,4 ms | −2,6 ms | ICMP CPE-servidor; 42.725 muestras; anexo 3 | CUMPLE |
| Jitter | ≤10 ms | 9,919450 ms | −0,080550 ms | TWAMP ponderado; 42.725 muestras; anexo 4* | CUMPLE* |
| Pérdida | ≤0,5% mensual | No determinable; 0,31% parcial | No determinable | Solo 1-18 sep; cobertura nominal 60%; anexo 5 | EVIDENCIA INSUFICIENTE |
| Throughput | ≥180 Mbps | 180,75 Mbps | +0,75 Mbps | Cuatro iperf3 TCP en CPE; anexo 6 | CUMPLE |
| Respuesta | ≤60 min; 100% tickets | Máximo 66 min; 3/4 dentro de plazo | +6 min; cobertura de cumplimiento 75% | INC-2672; anexo 2 | NO CUMPLE |
| MTTR por incidente | ≤240 min; atribuibles | 55, 71 y 27 min**; Máx. conservador 75 min | −169 min en máximo de trabajo; −165 min conservador | Tickets y fin NMS; anexos 1-2 | CUMPLE |

* Cumplimiento con los agregados suministrados en el anexo 4 y la salvedad de procedencia y cadencia descrita en 4.2. La comparación exacta 9,919449970743… ≤ 10 evita que el redondeo o el promedio simple de bloques cambien el dictamen.

** Los valores de trabajo 55, 71 y 27 min utilizan bases temporales distintas. La sección 5.5 reconstruye ambos intervalos. Con un criterio uniforme y conservador desde el inicio NMS, los valores son 55, 75 y 30 min: todos cumplen. No se calcula un promedio entre incidentes para ocultar una eventual excedencia individual.

### 5 1 1 Veredicto global

NO CUMPLE. Se acreditan incumplimientos de disponibilidad y tiempo de respuesta. El cumplimiento de otras métricas no compensa estos resultados. La ausencia de evidencia mensual de pérdida impide afirmar su cumplimiento o incumplimiento; no invalida los incumplimientos documentados.

### 5 1 2 Conciliación de tiempos

Caída física observada = 210 + 55 + 105 + 75 + 30 = 475 min

Tiempo excluido = 210 + 105 = 315 min

Caída atribuible = 475 − 315 = 160 min

Las 475 muestras faltantes de ICMP coinciden numéricamente con los 475 minutos de caída física. La correspondencia temporal exige revisar timestamps; esa coincidencia no demuestra por sí sola pérdida de paquetes ni permite reconstruir la serie TWAMP.

### 5 2 Clasificación de caídas y disponibilidad

| Ev. | Intervalo de septiembre | Duración | Atribuible | Fundamento |
| --- | --- | --- | --- | --- |
| E1 | 03-sep; 02:00 a 05:30 | 210 min | 0 min | Mantención PE. Aviso 29-ago 10:00: 112 h antes. Duración 3 h 30 min ≤4 h/mes. Excluido por 6.1a; disponible según 6.2. |
| E2 | 09-sep; 14:12 a 15:07 | 55 min | 55 min | Corte de fibra por obras viales. No consta fuerza mayor declarada que habilite 6.1b. Atribuible al proveedor. |
| E3 | 15-sep; 10:40 a 12:25 | 105 min | 0 min | CPE sin energía durante corte eléctrico del cliente y sin UPS. Responsabilidad del cliente por 7.2; exclusión 6.1c y tratamiento 6.2. |
| E4 | 21-sep; 22:05 a 23:20 | 75 min | 75 min | Falla de tarjeta de línea del PE La Serena; reemplazo. Equipo del proveedor, sin exclusión aplicable. |
| E5 | 27-sep; 08:30 a 09:00 | 30 min | 30 min | Mantención de emergencia. Aviso 26-sep 18:00: 14 h 30 min antes, inferior a 72 h. No cumple 6.1a. |

E5 no se excluye por denominarse emergencia. El enunciado registra 14 h 30 min de anticipación, no 24 h; ambos valores quedarían bajo 72 h. E1 consume 210 de los 240 minutos mensuales permitidos de mantención programada. Los 30 min restantes no eximen a E5 del requisito de aviso.

### Cálculo paso a paso

1. T = 30 días × 24 h/día × 60 min/h = 43.200 min

2. D = 55 + 75 + 30 = 160 min = 2 h 40 min

3. Tiempo disponible contractual = 43.200 − 160 = 43.040 min

4. A = (43.040 / 43.200) × 100 = 99,6296296296…% ≈ 99,63%

5. Caída permitida = 43.200 × (1 − 0,999) = 43,2 min

6. Exceso = 160 − 43,2 = 116,8 min = 1 h 56 min 48 s

7. Desviación = 99,6296296296 − 99,9 = −0,2703703704 pp

La cláusula 6.2 exige mantener los 43.200 minutos en el denominador: E1 y E3 se consideran disponibles para el SLA. La disponibilidad física sin exclusiones sería 98,900463%, pero no es la base del crédito. El valor contractual cae en 99,5% ≤ A <99,9%; la cláusula 8.1 asigna 10%.

### 5 3 Latencia jitter y pérdida

### Latencia

Cobertura = 42.725 / 43.200 × 100 = 98,900462963% ≥90%

RTT promedio = 27,4 ms ≤30 ms; margen = 30 − 27,4 = 2,6 ms

CUMPLE. El promedio de 27,4 ms se toma del agregado de Zabbix; no se dispone de muestras individuales para recomputarlo. El p95 de 41,2 ms y el máximo de 118 ms describen dispersión, pero el SLA no fija límites de percentil o máximo. El promedio de 22,1 ms PE-core se descarta por punto y destino distintos de los pactados.

### Jitter ponderado por muestras válidas

| Bloque | Días | Muestras nᵢ | Promedio Jᵢ | Producto nᵢ × Jᵢ |
| --- | --- | --- | --- | --- |
| 01 a 07-sep | 7 | 9.870 | 9,0 ms | 88.830,0 |
| 08 a 14-sep | 7 | 10.025 | 10,5 ms | 105.262,5 |
| 15 a 21-sep | 7 | 9.900 | 13,8 ms | 136.620,0 |
| 22 a 30-sep | 9 | 12.930 | 7,2 ms | 93.096,0 |
| Total | 30 | 42.725 | No aplica | 423.808,5 |

1. N = 9.870 + 10.025 + 9.900 + 12.930 = 42.725 muestras

2. S = 88.830 + 105.262,5 + 136.620 + 93.096 = 423.808,5

3. J = Σ(nᵢ × Jᵢ) / Σnᵢ = 423.808,5 / 42.725

4. J = 9,919449970743… ms ≈ 9,92 ms ≤10 ms → CUMPLE

El margen es 0,080550029257 ms. El promedio simple de los cuatro bloques sería 10,125 ms y produciría un dictamen incorrecto, porque asigna el mismo peso a bloques con distinto número de muestras. El último bloque comprende nueve días. El resultado es exacto respecto de los promedios tabulados; su precisión instrumental no puede verificarse sin datos crudos.

### Pérdida de paquetes

Cobertura temporal nominal = 18 / 30 × 100 = 60% <90%

Cobertura mínima = 30 × 0,90 = 27 días; déficit = 27 − 18 = 9 días

EVIDENCIA INSUFICIENTE. Solo consta 0,31% para el 1 al 18-sep. El colector se detuvo por disco lleno el 19-sep y no se recuperó. Faltan contadores de enviados y recibidos, secuencias, timestamps y registros válidos posteriores para completar al menos 90% del período. Sin respaldo recuperable no es posible validar retroactivamente el mes. El 0,18% del proveedor no subsana el vacío porque corresponde a PE-core.

### 5 4 Throughput

| Fecha | Prueba válida | Resultado |
| --- | --- | --- |
| 05-sep | iperf3 TCP, cuatro flujos, 60 s; LAN del CPE | 186 Mbps |
| 12-sep | iperf3 TCP, cuatro flujos, 60 s; LAN del CPE | 182 Mbps |
| 19-sep | iperf3 TCP, cuatro flujos, 60 s; LAN del CPE | 171 Mbps |
| 26-sep | iperf3 TCP, cuatro flujos, 60 s; LAN del CPE | 184 Mbps |

1. Umbral = 0,90 × 200 = 180 Mbps

2. Suma = 186 + 182 + 171 + 184 = 723 Mbps

3. Promedio = 723 / 4 = 180,75 Mbps ≥180 Mbps → CUMPLE

4. Proporción del contratado = 180,75 / 200 × 100 = 90,375%

El margen es 0,75 Mbps, equivalente a 0,375 pp sobre el mínimo de 90%. La prueba de 171 Mbps merece revisión operativa, pero el contrato evalúa el promedio mensual. El Speedtest de 95 Mbps del 18-sep queda fuera del cálculo. Deben conservarse comandos, salida JSON, dirección de tráfico y condiciones de carga para verificar la simetría del servicio.

### 5 5 Respuesta y restauración por incidente

| Ticket | Apertura | Primera respuesta | Respuesta | Veredicto ≤60 min |
| --- | --- | --- | --- | --- |
| INC-2611 | 09-sep 14:18 | 14:41 | 23 min | CUMPLE |
| INC-2648 | 15-sep 10:47 | 11:20 | 33 min | CUMPLE |
| INC-2672 | 21-sep 22:09 | 23:15 | 66 min | NO CUMPLE |
| INC-2690 | 27-sep 08:33 | 08:40 | 7 min | CUMPLE |

Respuesta = primera respuesta − apertura. Para INC-2672: 23:15 − 22:09 = 66 min; exceso = 66 − 60 = 6 min. Cumplen 3/4 tickets = 75%, inferior al 100% exigido por 4.1. El origen cliente de INC-2648 excluye su restauración, pero no la respuesta: 4.1 se refiere a todos los incidentes.

| Ticket | Restauración | Desde apertura | Desde inicio NMS | MTTR de trabajo |
| --- | --- | --- | --- | --- |
| INC-2611 | 15:07 | 49 min | 55 min | 55 min; cumple |
| INC-2648 | 12:25 | 98 min | 105 min | No aplica; cliente |
| INC-2672 | 23:20 | 71 min | 75 min | 71 min; cumple |
| INC-2690 | 09:00 | 27 min | 30 min | 27 min; cumple |

El extracto 4.2 no define el instante inicial. Los valores de trabajo 55/71/27 min mezclan inicio de caída en INC-2611 y apertura en los otros dos. Se muestran sin ocultar esa diferencia y se verifica la cota uniforme NMS: máximo 75 min ≤240 min. La disponibilidad siempre usa 55+75+30 min, sin sustituirlos por tiempos desde ticket.

## 6 Análisis de incumplimientos

| Hallazgo y fecha | Causa y origen | Impacto y efecto |
| --- | --- | --- |
| Disponibilidad; E2, 09-sep; 55 min | Corte de fibra de acceso por obras viales. Atribución al proveedor sin exclusión documentada. | Interrupción del enlace contratado; afecta conectividad de ERP, trazabilidad y voz que dependan de él. Aporta 55 min a la caída atribuible mensual. |
| Disponibilidad; E4, 21-sep; 75 min | Falla de tarjeta de línea en PE La Serena. Origen en equipamiento del proveedor. | Pérdida de conectividad durante 75 min. Principal contribución individual a los 160 min atribuibles. |
| Disponibilidad; E5, 27-sep; 30 min | Mantención de emergencia con aviso de 14 h 30 min. Gestión de cambios del proveedor sin requisito de exclusión. | Interrupción de 30 min contabilizada. La urgencia del trabajo no elimina el compromiso de disponibilidad. |
| Tiempo de respuesta; INC-2672, 21-sep | Primera respuesta a los 66 min. No hay evidencia suficiente para determinar la causa organizacional del retraso. | Incumplimiento de 6 min del plazo de atención; genera crédito adicional de 5%. No implica incumplimiento del tiempo de restauración. |

El impacto probado es la indisponibilidad del enlace y el retraso de primera respuesta. No se aportan registros para cuantificar pérdidas económicas, toneladas exportadas afectadas, transacciones fallidas o llamadas interrumpidas. Esos efectos deben contrastarse con bitácoras de las aplicaciones y de la operación de planta.

La falla de energía E3 es una interrupción real de 105 min, pero se excluye del crédito por responsabilidad del cliente. La caída del colector desde el 19-sep es una falla de observabilidad del cliente; impide verificar pérdida y requiere una acción correctiva independiente del reclamo al proveedor.

## 7 Conclusiones técnicas y crédito

El incumplimiento global se sustenta en 99,6296296296% de disponibilidad y una respuesta de 66 min. Latencia, jitter bajo la salvedad indicada, throughput y restauración cumplen. La pérdida permanece sin dictamen mensual por insuficiencia de evidencia.

| Concepto | Regla aplicada | Porcentaje | Monto neto |
| --- | --- | --- | --- |
| Disponibilidad | 8.1: 99,5% ≤99,62963% <99,9% | 10% | $120.000 |
| Tiempo de respuesta | 8.2: un incumplimiento acreditado | 5% | $60.000 |
| Otras métricas | Sin incumplimiento demostrado | 0% | $0 |
| Total aplicable | 8.3: 15% <tope de 50% | 15% | $180.000 |

Crédito porcentual = min(10% + 5%, 50%) = 15%

Crédito neto = 0,15 × $1.200.000 = $180.000

El tope equivale a $600.000; no es un crédito automático. No corresponde sumar 5% por cada caída ni cobrar por la pérdida no demostrada. El importe calculado es neto; no se añade IVA al monto solicitado en este dictamen.

### 7 1 Respuesta técnica al gerente de operaciones

| Afirmación o solicitud | Evaluación | Fundamento |
| --- | --- | --- |
| El enlace se cayó varias veces | Se sostiene | El NMS registra cinco interrupciones y 475 min físicos. Solo E2, E4 y E5 son atribuibles para el SLA: 160 min. E1 y E3 se excluyen. |
| Speedtest de 95 Mbps prueba incumplimiento de los 200 Mbps | No se sostiene como prueba contractual | Se realizó en notebook por Wi-Fi con herramienta no pactada. Las cuatro pruebas iperf3 en CPE promedian 180,75 Mbps y cumplen el mínimo de 180 Mbps. |
| Peaks de 118 ms prueban incumplimiento de latencia | No se sostiene con el estadístico pactado | La cláusula 3.2 evalúa RTT promedio mensual ≤30 ms. El promedio válido es 27,4 ms. Los peaks justifican diagnóstico, no ese crédito. |
| Se debe exigir el crédito máximo de 50% | No se sostiene | El tramo de disponibilidad otorga 10%; la respuesta tardía añade 5%. Total 15% = $180.000 neto. La diferencia respecto del máximo solicitado es $420.000. |

Gerencia de Operaciones: corresponde reclamar a NorteNet $180.000 neto por septiembre. La solicitud debe adjuntar la clasificación de E2, E4 y E5, sus 160 minutos de caída atribuible y el ticket INC-2672, cuya primera respuesta excedió el plazo en seis minutos. Los resultados de Speedtest y los máximos de Zabbix se pueden adjuntar como antecedentes de diagnóstico, identificando que no determinan los créditos contractuales.

La ausencia de medición mensual válida de pérdida debe comunicarse expresamente. El crédito calculado se apoya en la evidencia disponible; cualquier revisión exige nuevos registros válidos en la demarcación. No corresponde presentar 0,31% o 0,18% como pérdida mensual acreditada del enlace.

### 7 2 Expediente de reclamación

Adjuntar el extracto de cláusulas 3.1, 4.1 y 8.1 a 8.4; el registro NMS de los tres eventos atribuibles; los diagnósticos y marcas de tiempo de los tickets; el aviso de E5; la tabla de cálculo; y la salida reproducible de la calculadora. Solicitar confirmación del crédito y un plan correctivo con responsable y fecha comprometida. El extracto no informa plazo ni canal formal para reclamar; deben verificarse en el contrato completo antes del envío.

## 8 Recomendaciones y anexos

### 8 1 Acciones priorizadas

| Prioridad | Acción y responsable propuesto | Criterio de cierre |
| --- | --- | --- |
| Alta; Inmediata | TI del cliente: recuperar el colector, liberar capacidad controladamente, definir retención y alertas de disco, proceso y ausencia de muestras. | Prueba de alertas y exportación de registros; cobertura ≥90% en el siguiente período. Recuperar respaldo de septiembre si existe. |
| Alta; Inmediata | NorteNet: corregir el escalamiento de incidentes y exigir acuse dentro de 60 min. Revisar INC-2672. | Causa del retraso documentada; escalamiento preventivo antes del límite y seguimiento del 100% de tickets. |
| Alta; Antes de ampliar el servicio | NorteNet y TI: diseñar respaldo de acceso con ruta diversa, energía protegida y conmutación probada. Validar radioenlace propuesto. | Disponibilidad de diseño ≥99,9%, capacidad y calidad pactadas durante respaldo, tiempo de conmutación medido y aceptación conjunta. |
| Alta; Próximo ciclo operativo | Cliente: instalar y mantener UPS del CPE y del acceso de respaldo, con autonomía definida según los cortes de planta. | Prueba bajo carga y corte de suministro; autonomía y alarmas documentadas. No se dimensiona una UPS sin potencia y duración requeridas. |
| Alta; Antes del siguiente cierre | TI y NorteNet: verificar procedencia del jitter, cadencia TWAMP, puntos de prueba y sincronización temporal. Acordar inicio del tiempo de restauración. | Sesiones y colectores identificados; timestamps trazables; definición única de restauración aceptada. |
| Media; Siguiente mantención | NorteNet: revisar protección de fibra frente a obras, repuestos de PE y procedimiento de cambios. | Acciones sobre E2/E4; avisos programados ≥72 h y control del máximo de 4 h/mes. |
| Media; Siguiente mes | TI y NorteNet: repetir iperf3 en ambas direcciones y revisar el margen de 0,75 Mbps; analizar p95 y peaks de latencia. | Al menos cuatro pruebas válidas por mes, salidas JSON y dirección identificada. Revisar QoS/ruta sin afirmar causas no probadas. |
| Media; Revisión del SLA | Gestor del servicio: acordar tratamiento de fuerza mayor, evidencia alternativa, percentiles de latencia y condiciones de respaldo. | Adenda con métricas, métodos, responsables y revisión periódica. Los nuevos objetivos no se aplican retroactivamente. |

La revisión de niveles de servicio debe mantener un registro de acciones, responsable, fecha y evidencia de cierre. En términos de ITIL 4, se vinculan el seguimiento del SLA, la gestión de incidentes, problemas y cambios. La verificación del resultado y el ajuste posterior se integran a la mejora del sistema de gestión de servicios de ISO/IEC 20000-1.

### 8 2 Anexo A Viabilidad de la infraestructura

Las disponibilidades del anexo 7 son anuales. Se usan como parámetros de un modelo de planificación, bajo comportamiento estable e independencia de fallas; no sustituyen la disponibilidad mensual medida ni garantizan cada mes. Las cifras se convierten a fracciones antes de operar.

| Componente | Disponibilidad | Fracción |
| --- | --- | --- |
| CPE | 99,95% | 0,9995 |
| Fibra de acceso de ruta única | 99,80% | 0,9980 |
| PE La Serena | 99,99% | 0,9999 |
| Backbone | 99,99% | 0,9999 |
| Radioenlace de acceso ofrecido | 99,50% | 0,9950 |

### Ruta única en serie

Aserie = ACPE × Afibra × APE × Abackbone

Aserie = 0,9995 × 0,9980 × 0,9999 × 0,9999 = 0,99730150977501

Aserie = 99,730150977501% ≈ 99,73% <99,9%

Caída equivalente = (1 − 0,99730150977501) × 43.200 = 116,574778 min

El diseño queda 0,169849 pp bajo el objetivo; la caída equivalente supera en 73,374778 min el presupuesto de 43,2 min. Es una proyección bajo los supuestos anteriores, no otra caída observada en septiembre. Además, la disponibilidad de un sistema en serie no supera la de su componente más débil: la fibra de 99,80% ya limita el diseño, incluso sin aplicar independencia.

### Fibra y radio en paralelo con elementos comunes en serie

Aacceso = 1 − (1 − Afibra) × (1 − Aradio)

Aacceso = 1 − (0,0020 × 0,0050) = 0,99999 = 99,999%

Atotal = 0,9995 × 0,99999 × 0,9999 × 0,9999

Atotal = 0,99929011699390005 = 99,92901169939%

Caída equivalente = (1 − Atotal) × 43.200 = 30,666946 min

El modelo supera 99,9% y deja un margen equivalente de 12,533054 min frente al presupuesto mensual. CPE, PE y backbone permanecen comunes; el respaldo de acceso no elimina una falla de tarjeta en el mismo PE. Tampoco corrige la falta de UPS del cliente.

La cifra ideal de 99,998650754888%, obtenida al poner toda la cadena actual en paralelo con 99,50%, solo aplicaría si el radio fuese un servicio completo e independiente. El anexo lo ofrece como acceso, por lo que esa cifra no se utiliza para recomendar la contratación.

La ruta única no respalda por sí sola el objetivo de diseño. Se requiere mejorar la disponibilidad del acceso o añadir redundancia; el radio es una alternativa, no la única solución posible. Antes de contratar deben acreditarse diversidad física, independencia de fallas, capacidad útil, QoS, energía y conmutación. Sin esos datos y sin precio del respaldo no puede afirmarse garantía mensual ni rentabilidad económica.

### 8 3 Anexo B Aplicación reproducible del toolkit

El paquete adjunto incluye objetivos.yaml, CSV, calculadora, pruebas y salida ejecutada. Los CSV transcriben los anexos del caso; no se presentan como exportaciones originales. La calculadora compara sin redondeos intermedios, retiene la cobertura de pérdida y pondera el jitter por número de muestras.

| Ruta dentro del repositorio | Contenido |
| --- | --- |
| README.md y CHANGELOG.md | Uso, requisitos, cambios y pendientes para v1.1 |
| docs/ | Método, referencias y glosario |
| plantillas/ y formulas/ | Plantillas reutilizables y fórmulas con variables y ejemplos |
| herramientas/objetivos.yaml | Objetivos, coberturas, créditos y supuestos del caso |
| herramientas/calc_sla.py | Verificación de siete métricas y cálculo del crédito |
| ejemplos/caso-valle-elqui/ | sla.md, mediciones.csv, eventos.csv, tickets.csv, evidencia_descartada.csv e informe.md |
| ejemplos/caso-valle-elqui/ | salida_calc_sla.txt, resultados.json y registro de pruebas |
| tests/test_calc_sla.py | Pruebas de límites, cobertura, ponderación y tope |

### Ejecución y salida obtenida

```text
python3 herramientas/calc_sla.py \
  -o herramientas/objetivos.yaml \
  -m ejemplos/caso-valle-elqui/mediciones.csv
```

```text
PERIODO 2026-09
METRICA         MEDIDO              VEREDICTO
disponibilidad  99.629630 %         NO CUMPLE
latencia        27.400000 ms        CUMPLE
jitter          9.919450 ms         CUMPLE
perdida         No determinable     EVIDENCIA INSUFICIENTE
throughput      180.750000 Mbps     CUMPLE
respuesta       66.000000 min       NO CUMPLE
mttr            75.000000 min       CUMPLE
GLOBAL: NO CUMPLE
CREDITO: 15.00% = CLP 180000 neto
Jitter: anexo 4 aceptado; verificar origen y cadencia.
MTTR: cota conservadora NMS; valores 55, 75 y 30 min.
Perdida: cobertura parcial 60%; no genera credito demostrado.
```

La restauración de 75 min de esta salida es la cota conservadora NMS. No contradice los valores de trabajo 55/71/27 min: utiliza un origen temporal uniforme, documentado en objetivos.yaml. La salida no asigna cumplimiento a datos ausentes ni calcula crédito por una pérdida sin cobertura suficiente.

Validación ejecutada: cinco pruebas satisfactorias. Se verificaron el crédito del caso y la ponderación, el límite inclusivo de respuesta de 60 min, la falta de una prueba de throughput, la ausencia de jitter y los límites del tramo de disponibilidad y del tope de crédito.

### 8 4 Anexo C Integración y versionado

### 8 4 Anexo C Integración y versionado

El código, las mediciones y el informe del caso se mantienen en el repositorio del toolkit. La ejecución de la calculadora y las pruebas se documenta en el anexo B.

| Campo de entrega | Identificación |
| --- | --- |
| Repositorio | https://github.com/JoseTapiaIna/sla-toolkit-tapia |
| Ruta del caso | ejemplos/caso-valle-elqui/ |
| Etiqueta de entrega | v1.1 |
| Integrante | Jose Alberto Tapia Cerda |
| Licencia del código | MIT |

Las correcciones se registran en CHANGELOG.md y se integran a main mediante una rama de trabajo. La etiqueta de entrega debe apuntar al commit que contiene los archivos verificados.

Las mejoras futuras incluyen la ingestión de registros crudos, el cálculo de cobertura mediante timestamps y la verificación de ambas direcciones de throughput.

### 8 5 Anexo D Datos necesarios para cerrar las salvedades

Para pérdida: recuperar los registros posteriores al 18-sep o un conjunto alternativo desde la misma demarcación, con enviados, recibidos y timestamps que cubran al menos 90% del mes. Para jitter: identificar el colector y la sesión que generaron los bloques posteriores al 19-sep y confirmar la cadencia. Para MTTR: acordar por escrito el origen y el hito de restauración. Para throughput: identificar dirección, servidor, parámetros y condiciones de carga de cada ejecución.

Para la solución de respaldo: solicitar topología, puntos comunes, disponibilidad aplicable al acceso, capacidad, QoS, tiempo de conmutación, protección eléctrica y cotización. La aceptación debe incorporar una prueba de caída de fibra y recuperación por radio con tráfico de los servicios críticos.

### 8 6 Anexo E Fuentes y trazabilidad

### Documentos del caso

| ID | Documento y uso |
| --- | --- |
| F1 | EVA 3 CASO DE ESTUDIO.pdf. P. 1: contexto y correo; p. 2: contrato; p. 3: anexos 1-4; p. 4: anexos 5-7; pp. 5-6: tareas, estructura y rúbrica. Fuente de cifras y cláusulas. |
| F2 | PautaToolkit_SLA.pdf. Método, normas, estructura del repositorio y requisitos de calculadora y versionado. |
| F3 | Caso_Clinica_Limari.pdf. Referencia metodológica para la estructura del informe y la aplicación del toolkit. Sus cifras y cláusulas no se trasladan al caso Valle de Elqui. |
| F4 | SLA y niveles de servicio en redes.pdf. Material docente de métricas, exclusiones, fórmulas y disponibilidad en serie y paralelo. |

### Referencias técnicas primarias

[N1] PeopleCert. ITIL 4 Practitioner Service Level Management.

https://www.peoplecert.org/ITIL4-practices

[N2] ISO/IEC 20000-1:2018. Service management system requirements. Referencia al marco de gestión.

https://www.iso.org/standard/70636.html

[N3] ITU-T E.860 (06/2002). Framework of a service level agreement.

https://www.itu.int/rec/T-REC-E.860

[N4] ITU-T Y.1540 (12/2019). IP packet transfer and availability performance parameters.

https://www.itu.int/rec/T-REC-Y.1540/en

[N5] RFC 3393 (2002). IP Packet Delay Variation Metric for IPPM.

https://www.rfc-editor.org/rfc/rfc3393.html

[N6] RFC 5357 (2008). A Two-Way Active Measurement Protocol.

https://www.rfc-editor.org/rfc/rfc5357.html

[N7] RFC 6349 (2011). Framework for TCP Throughput Testing.

https://www.rfc-editor.org/rfc/rfc6349.html

Consulta de referencias técnicas: 4 de noviembre de 2026. Los métodos se aplican conforme al extracto contractual; las referencias normativas no alteran el período, las exclusiones o los porcentajes de crédito del caso.

### Criterio de lectura de resultados

CUMPLE: evidencia aceptada y valor dentro del objetivo. NO CUMPLE: evidencia suficiente de una excedencia contractual. EVIDENCIA INSUFICIENTE: no se dispone de datos válidos para decidir. Los supuestos se identifican donde afectan la cobertura o el modelo; las hipótesis de diseño no se presentan como mediciones operativas.
