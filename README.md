# Toolkit de verificación de SLA de Agrícola Valle de Elqui

Toolkit académico para verificar el SLA del enlace dedicado de 200 Mbps de Agrícola Valle de Elqui SpA, contratado a NorteNet durante septiembre de 2026.

Incluye objetivos contractuales, mediciones transcritas del caso, calculadora, pruebas, resultados e informe técnico.

Autor: Jose Alberto Tapia Cerda.

## Ejecución

Requiere Python 3.10 o superior y PyYAML 6.x. Desde la raíz:

```bash
python3 -m pip install -r requirements.txt
python3 herramientas/calc_sla.py -o herramientas/objetivos.yaml -m ejemplos/caso-valle-elqui/mediciones.csv --json ejemplos/caso-valle-elqui/resultados.json
python3 -m unittest discover -s tests
```

La pérdida parcial conserva su cobertura de 60% y no se convierte en cumplimiento. El jitter se pondera por muestras, sin redondearlo antes de comparar. Los tiempos de respuesta se verifican por máximo y cobertura completa de tickets. La restauración se evalúa con la duración total NMS, más conservadora que la duración desde apertura del ticket.

## Límites y publicación

Los CSV son transcripciones de los anexos del enunciado, no exportaciones originales. La frecuencia de jitter de 60 s es un supuesto para cuantificar cobertura; se debe verificar la independencia respecto del colector de pérdida. El expediente mezcla bases para MTTR: el informe muestra ambas. No hay URL de repositorio ni tag publicado acreditados en este paquete.

Integrar la carpeta ejemplos/caso-valle-elqui y los cambios de herramientas en el toolkit existente. Revisar compatibilidad antes de sustituir archivos. Seguir los comandos del informe para publicar v1.1 una vez identificado el remoto. No sobrescribir un tag v1.1 existente.
