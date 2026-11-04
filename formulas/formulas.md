# Fórmulas aplicadas

## Disponibilidad y crédito
A = (T - D) / T × 100. T = minutos del período; D = caída atribuible. Fuente: definición operativa de disponibilidad y cláusulas 3.1, 6.1, 6.2. Ejemplo: (43200-160)/43200×100 = 99.6296296296%.
D_permitida = T×(1-A_obj/100) = 43.2 min; exceso = 160-43.2 = 116.8 min.
Crédito = min(crédito por tramo + suma de créditos demostrados, tope) × cargo. Fuente: cláusulas 8.1 a 8.4. Ejemplo: (10%+5%)×1200000 = 180000 CLP neto.

## Agregados de calidad
RTT_promedio = suma de RTT válidos / número de muestras válidas. El anexo ya entrega 27.4 ms; no hay datos crudos para recalcularlo.
J_promedio = suma(n_i×J_i)/suma(n_i). Agregación estadística de promedios comparables de variación del retardo (RFC 3393). Ejemplo: 423808.5/42725 = 9.919449970743 ms.
Throughput medio = suma(x_i)/n = 723/4 = 180.75 Mbps; proporción del contratado = 180.75/200×100 = 90.375%. Referencia metodológica TCP: RFC 6349; el umbral 90% proviene del contrato.
Pérdida = paquetes no recibidos / paquetes enviados ×100. Medición activa: RFC 5357. Ejemplo ilustrativo: 5/1000×100 = 0.5%. El caso carece de contadores mensuales completos.

## Arquitectura
A_serie = producto(A_i), bajo independencia. Ejemplo: .9995×.998×.9999² = .99730150977501.
A_paralelo = 1-producto(1-A_i), con fallas independientes y conmutación disponible. Ejemplo para fibra y radio: 1-(1-.998)(1-.995)=.99999. Mantener componentes comunes en serie.
Son modelos de confiabilidad, no garantías mensuales ni fórmulas impuestas por E.860.

## Latencia física
t_propagación = distancia / velocidad. Con velocidad aproximada de 200000 km/s en fibra, 100 km implican 0.5 ms en un sentido y 1 ms de propagación RTT; no incluye enrutamiento, colas ni procesamiento. Es una estimación física ilustrativa, no una medición del caso.
