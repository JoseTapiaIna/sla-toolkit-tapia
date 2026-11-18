# EVA 3 — Paquete corregido antes de la entrega

**Autor:** Jose Alberto Tapia Cerda
**Sección:** 2026/P DCIT06/D-CT0-N6-P3-C1/D La Serena CT
**Repositorio:** https://github.com/JoseTapiaIna/sla-toolkit-tapia

## Qué se corrigió

- En sección 4: cálculo de cobertura para cada tipo de evidencia, lista explícita de información faltante y fuentes descartadas.
- En sección 5: tabla por ticket para respuesta y MTTR, y explicación de latencia/pérdida.
- En sección 6: fechas, hechos, causa, origen e impacto operacional por cada incumplimiento.
- En sección 9: comandos exactos, pasos manuales/automáticos, declaración de IA y limitaciones del nivel básico de automatización.
- En carpeta del caso: copia `objetivos.yaml` y `salida_calc.txt` con los nombres de la pauta.
- El título de sección 7 y la sección de la portada ya estaban corregidos en la versión previa; se conservan.
- Se incorporan las capturas reales y la salida completa. **No se alteran los datos contractuales ni los códigos de la calculadora existentes.**

## 1. Preparar Ubuntu (sin publicar todavía)

Desde Ubuntu WSL, usando tu cuenta habitual:

```bash
cd ~/sla-toolkit-tapia
cp ejemplos/caso-valle-elqui/informe.md ~/informe_anterior_eva3.md
explorer.exe .
```

En el Explorador de Windows, copiar **el ZIP nuevo** dentro de esta carpeta (raíz del repositorio). Después:

```bash
sudo apt update
sudo apt install -y pandoc libreoffice-writer unzip
unzip -o Paquete_EVA3_CORREGIDO_Jose_Tapia.zip
source ~/eva3-sla-venv/bin/activate
bash generar_informe.sh
```

Debe aparecer `OK: matriz y crédito coherentes con resultados.json`, `Ran 5 tests ... OK` y `OK: archivos verificados`.

**Nota:** el script utiliza el nivel básico de automatización: recalcula, valida cifras principales y exporta desde Markdown. Si cambian los datos o el contrato, el análisis redactado requiere revisión manual. El validador detiene la exportación si detecta incoherencias en la matriz principal.

## 2. Revisar antes de publicar

```bash
git status
explorer.exe ejemplos/caso-valle-elqui
```

Abrir `informe.pdf` y comprobar portada, tablas, capturas y anexos. No publicar si algo está mal.

## 3. Publicación en GitHub: solo después de aprobar la revisión

```bash
git switch main
git add INSTRUCCIONES_ENTREGA.md generar_informe.sh validar_consistencia.py ejemplos/caso-valle-elqui
git commit -m "docs: finaliza informe EVA3 conforme a la pauta"
git push origin main
```

**Etiqueta v1.1:** ya existe y se usa en la portada. No se debe forzar la etiqueta remotamente sin antes comprobar qué commit está publicado y si otras personas utilizan la versión. Una etiqueta nueva de corrección puede ser más segura, pero si la entrega exige exactamente `v1.1`, habrá que acordar cómo actualizarla y preservar la referencia anterior. Este paso no se ejecuta automáticamente.

## Verificación rápida del contenido

Se deben hallar las nueve secciones, la salida de `calc_sla.py`, `objetivos.yaml`, `mediciones.csv`, desglose por tickets, las 8 capturas, pruebas unitarias y declaraciones de IA. El PDF debe salir del Markdown con `bash generar_informe.sh`.
