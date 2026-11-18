#!/usr/bin/env python3
"""Verifica que las cifras publicadas en la matriz principal coincidan con resultados.json."""
import json
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

c = Path(__file__).resolve().parent / 'ejemplos' / 'caso-valle-elqui'
data = json.loads((c / 'resultados.json').read_text(encoding='utf-8'))
md = (c / 'informe.md').read_text(encoding='utf-8')

def fmt(key, digits=2):
    x = Decimal(str(data['resultados'][key]['medido']))
    q = Decimal('1').scaleb(-digits)
    return format(x.quantize(q, rounding=ROUND_HALF_UP), f'.{digits}f').replace('.', ',')

rows={}
for line in md.splitlines():
    if line.startswith('|'):
        fields=[x.strip().replace('**','') for x in line.strip().strip('|').split('|')]
        if len(fields)>=3:
            rows.setdefault(fields[0],[]).append(fields)

checks={
    'Disponibilidad': fmt('disponibilidad',2)+'%',
    'Latencia RTT': fmt('latencia',1)+' ms',
    'Jitter': fmt('jitter',2)+' ms',
    'Throughput': fmt('throughput',2)+' Mbps',
    'Respuesta': fmt('respuesta',0)+' min',
    'MTTR': fmt('mttr',0)+' min',
}
errors=[]
for label, measured in checks.items():
    matching=[x for x in rows.get(label,[]) if len(x)>=7]
    if not matching or not any(measured == x[2] for x in matching):
        errors.append(f'Matriz {label}: debería mostrar {measured}')
# Do not treat packet loss with partial coverage as a valid metric.
if not any('No determinable' in x[2] for x in rows.get('Pérdida',[]) if len(x)>=7):
    errors.append('La pérdida mensual debe aparecer como No determinable')
if data['veredicto_global'] != 'NO CUMPLE':
    errors.append('Veredicto global distinto del documento')
credit=Decimal(str(data['credito_porcentaje']))
clp=Decimal(str(data['credito_neto_clp']))
if credit != Decimal('15') or clp != Decimal('180000'):
    errors.append('El crédito cambió; revisar el análisis contractual y actualizar el Markdown')
if errors:
    raise SystemExit('ERROR: informe.md no coincide con el cálculo:\n - '+'\n - '.join(errors))
print('OK: matriz y crédito coherentes con resultados.json.')
