import yaml

def evaluar_sla():
    print("--- Herramienta de Calculo de SLA - Toolkit INACAP ---")
    with open("objetivos.yaml", "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    print(f"Servicio evaluado: {config['servicio']}")
    print("Umbrales cargados correctamente. Validando métricas...")

if __name__ == "__main__":
    evaluar_sla()