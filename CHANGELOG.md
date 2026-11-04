# Historial de cambios

## [1.1] - 2026-11-04

### Agregado
- Caso de Agrícola Valle de Elqui de septiembre de 2026.
- Objetivos, mediciones, eventos, tickets y fuentes descartadas.
- Jitter ponderado por muestras y verificación de cobertura.
- Respuesta por incidente, restauración conservadora y créditos con tope.
- Salida real en texto y JSON; pruebas de regresión de límites y datos faltantes.

### Corregido
- Incorporación de requirements.txt para instalar las dependencias.
- Adaptación del CSV de ejemplo al formato de la calculadora.
- Incorporación de licencia MIT.
- Actualización de referencias al repositorio y datos del autor.
- Eliminación del encabezado duplicado en el informe.

### Versionado
La corrección de la etiqueta v1.1 se realiza después de validar la entrega. La versión inicialmente etiquetada se conserva como v1.1-inicial.

### Mejoras futuras
- Ingesta de telemetría cruda y cobertura temporal por timestamps sin asumir cadencia.
- Clasificación asistida de exclusiones mediante avisos y tickets.
- Cómputo automático de intervalos desde marcas temporales y zona horaria declarada.
- Confirmar sesiones TWAMP independientes y ambas direcciones de throughput.
