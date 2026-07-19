# Definição de limites físicos/agronômicos reais e coerentes
LIMITES_AGRONOMICOS = {
    'N': {'min': 0, 'max': 150, 'label': 'Nitrogênio (mg/kg)'},
    'P': {'min': 5, 'max': 150, 'label': 'Fósforo (mg/kg)'},
    'K': {'min': 5, 'max': 210, 'label': 'Potássio (mg/kg)'},
    'temperature': {'min': 5.0, 'max': 50.0, 'label': 'Temperatura (°C)'},
    'humidity': {'min': 10.0, 'max': 100.0, 'label': 'Umidade (%)'},
    'ph': {'min': 3.5, 'max': 10.0, 'label': 'pH do Solo'},
    'rainfall': {'min': 20.0, 'max': 350.0, 'label': 'Pluviosidade (mm)'}
}


def validar_dados_solo(dados):

    for chave, limites in LIMITES_AGRONOMICOS.items():
        val = dados.get(chave)
        if val is None:
            return False, f"O campo {limites['label']} é obrigatório."
        if val < limites['min'] or val > limites['max']:
            return False, f"O valor de {limites['label']} deve estar entre {limites['min']} e {limites['max']} para ser uma situação agrícola real."
    return True, None
