#!/usr/bin/env bash
# Regenera el PDF y el DOCX reproduciblemente desde el Markdown del caso.
set -euo pipefail
cd "$(dirname "$0")"
CASO="ejemplos/caso-valle-elqui"
command -v pandoc >/dev/null || { echo 'Instala pandoc: sudo apt install pandoc'; exit 1; }
command -v libreoffice >/dev/null || { echo 'Instala LibreOffice: sudo apt install libreoffice-writer'; exit 1; }
python3 -c 'import yaml' || { echo 'Falta PyYAML: pip install -r requirements.txt'; exit 1; }

# Se guarda una copia local para cumplir la estructura pedida sin divergir de la configuración canónica.
if ! cmp -s herramientas/objetivos.yaml "$CASO/objetivos.yaml"; then
  echo 'AVISO: se sincroniza la copia de objetivos.yaml con herramientas/objetivos.yaml'
  cp herramientas/objetivos.yaml "$CASO/objetivos.yaml"
fi
python3 herramientas/calc_sla.py -o "$CASO/objetivos.yaml" -m "$CASO/mediciones.csv" --json "$CASO/resultados.json" > "$CASO/salida_calc.txt"
cp "$CASO/salida_calc.txt" "$CASO/salida_calc_sla.txt"
python3 validar_consistencia.py
python3 -m unittest discover -s tests

pandoc "$CASO/informe.md" -f markdown+raw_html+raw_attribute -t docx --resource-path="$CASO" --reference-doc="$CASO/referencia_informe.docx" -o "$CASO/informe.docx"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
libreoffice -env:UserInstallation=file://"$TMP"/profile --headless --convert-to pdf --outdir "$TMP" "$CASO/informe.docx"
[ -s "$TMP/informe.pdf" ] || { echo 'ERROR: no se generó el PDF nuevo'; exit 1; }
mv "$TMP/informe.pdf" "$CASO/informe.pdf"
echo "OK: archivos verificados: $CASO/informe.md, informe.docx, informe.pdf"
