import copy, csv, importlib.util, unittest
from pathlib import Path
import yaml
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('calc',ROOT/'herramientas/calc_sla.py')
calc=importlib.util.module_from_spec(spec);spec.loader.exec_module(calc)

class Verificacion(unittest.TestCase):
    def setUp(self):
        self.obj=yaml.safe_load((ROOT/'herramientas/objetivos.yaml').read_text())
        with (ROOT/'ejemplos/caso-valle-elqui/mediciones.csv').open() as f:self.rows=list(csv.DictReader(f))
    def test_caso_y_ponderacion(self):
        r=calc.evaluar(self.obj,self.rows)
        self.assertEqual(calc.D(r['credito_neto_clp']),calc.D(180000))
        self.assertEqual(r['resultados']['jitter']['veredicto'],'CUMPLE')
        self.assertEqual(r['resultados']['perdida']['veredicto'],'EVIDENCIA INSUFICIENTE')
        self.assertLess(abs(calc.D(r['resultados']['jitter']['medido'])-calc.D('9.919449970743')),calc.D('0.000000000001'))
    def test_limite_respuesta_inclusivo(self):
        for row in self.rows:
            if row['metrica']=='respuesta' and row['valor']=='66':row['valor']='60'
        r=calc.evaluar(self.obj,self.rows)
        self.assertEqual(r['resultados']['respuesta']['veredicto'],'CUMPLE')
        self.assertEqual(calc.D(r['credito_neto_clp']),calc.D(120000))
    def test_falta_una_prueba(self):
        rows=[r for r in self.rows if not(r['metrica']=='throughput' and r['fecha']=='2026-09-26')]
        self.assertEqual(calc.evaluar(self.obj,rows)['resultados']['throughput']['veredicto'],'EVIDENCIA INSUFICIENTE')
    def test_dato_ausente_no_cumple_por_defecto(self):
        rows=[r for r in self.rows if r['metrica']!='jitter']
        self.assertEqual(calc.evaluar(self.obj,rows)['resultados']['jitter']['veredicto'],'EVIDENCIA INSUFICIENTE')
    def test_tramo_99_5_y_tope(self):
        rows=[r for r in self.rows if r['metrica']!='caida_atribuible']
        row=copy.deepcopy(self.rows[0]);row['valor']='216';rows.append(row)
        r=calc.evaluar(self.obj,rows)
        self.assertEqual(calc.D(r['credito_componentes']['disponibilidad']),calc.D('.1'))
        row['valor']='500'
        r=calc.evaluar(self.obj,rows)
        self.assertEqual(calc.D(r['credito_porcentaje']),calc.D('50'))

if __name__=='__main__':unittest.main()
