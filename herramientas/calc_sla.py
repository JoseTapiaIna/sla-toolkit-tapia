#!/usr/bin/env python3
"""Verifica el caso desde CSV y objetivos YAML. No genera mediciones de red."""
import argparse, csv, json
from decimal import Decimal, getcontext
from pathlib import Path
import yaml
getcontext().prec = 32
D = lambda x: Decimal(str(x))

def evaluar(obj, rows):
    total=D(obj['minutos_periodo']); mincov=D(obj['cobertura_minima'])
    grouped={}
    for r in rows:
        if r['valida'].strip().lower()=='si':
            grouped.setdefault(r['metrica'],[]).append(r)
    resultados={}
    for met, rule in obj['metricas'].items():
        rr=grouped.get('caida_atribuible' if met=='disponibilidad' else met,[])
        value=None; sufficient=bool(rr); cov=None
        vals=[D(r['valor']) for r in rr]
        if met=='disponibilidad' and rr:
            cov=min(D(r['cobertura']) for r in rr)
            value=(total-sum(vals))/total*100
            sufficient=cov>=mincov
        elif met=='latencia' and rr:
            nn=sum(D(r['muestras_validas']) for r in rr)
            expected=D(rr[0]['muestras_esperadas'])
            cov=nn/expected; sufficient=cov>=mincov
            value=sum(D(r['valor'])*D(r['muestras_validas']) for r in rr)/nn
        elif met=='jitter' and rr:
            nn=sum(D(r['muestras_validas']) for r in rr)
            cov=nn/D(rr[0]['muestras_esperadas']); sufficient=cov>=mincov
            value=sum(D(r['valor'])*D(r['muestras_validas']) for r in rr)/nn
        elif met=='perdida' and rr:
            cov=D(rr[0]['cobertura']); sufficient=cov>=mincov and len(rr)==1
            # El agregado disponible es parcial; no se renombra como dato mensual.
            value=vals[0] if sufficient else None
        elif met=='throughput' and rr:
            sufficient=len(rr)>=rule['minimo_pruebas']; value=sum(vals)/len(vals)
        elif met in ('respuesta','mttr') and rr:
            cov=min(D(r['cobertura']) for r in rr)
            sufficient=cov==1; value=max(vals)
        target=D(rule['objetivo'])
        verdict='EVIDENCIA INSUFICIENTE'
        if sufficient and value is not None:
            verdict='CUMPLE' if (value>=target if rule['operador']=='>=' else value<=target) else 'NO CUMPLE'
        resultados[met]={'objetivo':str(target),'operador':rule['operador'],'unidad':rule['unidad'],
            'medido':str(value) if value is not None else None,
            'cobertura':str(cov) if cov is not None else None,'veredicto':verdict}
    credit=D(0); components={}
    a=resultados['disponibilidad']
    if a['veredicto']=='NO CUMPLE':
        for band in obj['creditos_disponibilidad']:
            if D(band['desde'])<=D(a['medido'])<D(band['hasta']):
                components['disponibilidad']=str(D(band['credito']));credit+=D(band['credito']);break
    for met in ('latencia','jitter','perdida','throughput','respuesta'):
        if resultados[met]['veredicto']=='NO CUMPLE':
            components[met]=str(D(obj['credito_otras']));credit+=D(obj['credito_otras'])
    credit=min(credit,D(obj['tope_credito']))
    global_result='NO CUMPLE' if any(r['veredicto']=='NO CUMPLE' for r in resultados.values()) else ('EVIDENCIA INSUFICIENTE' if any(r['veredicto']=='EVIDENCIA INSUFICIENTE' for r in resultados.values()) else 'CUMPLE')
    return {'periodo':obj['periodo'],'resultados':resultados,'credito_componentes':components,
        'credito_porcentaje':str(credit*100),'credito_neto_clp':str(credit*D(obj['cargo_mensual'])),
        'veredicto_global':global_result,'supuestos':obj['supuestos']}

def salida(result):
    lines=['PERIODO '+result['periodo'],'METRICA         MEDIDO              VEREDICTO']
    for met,r in result['resultados'].items():
        val='No determinable' if r['medido'] is None else f"{D(r['medido']):.6f} {r['unidad']}"
        lines.append(f"{met:<15} {val:<19} {r['veredicto']}")
    lines += ['GLOBAL: '+result['veredicto_global'],
        f"CREDITO: {D(result['credito_porcentaje']):.2f}% = CLP {D(result['credito_neto_clp']):.0f} neto",
        'Jitter: anexo 4 aceptado; verificar origen y cadencia.',
        'MTTR: cota conservadora NMS; valores 55, 75 y 30 min.',
        'Perdida: cobertura parcial 60%; no genera credito demostrado.']
    return '\n'.join(lines)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('-o','--objetivos',required=True);p.add_argument('-m','--mediciones',required=True);p.add_argument('--json')
    args=p.parse_args()
    obj=yaml.safe_load(Path(args.objetivos).read_text(encoding='utf-8'))
    with open(args.mediciones,encoding='utf-8',newline='') as f: rows=list(csv.DictReader(f))
    result=evaluar(obj,rows)
    if args.json: Path(args.json).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(salida(result))
