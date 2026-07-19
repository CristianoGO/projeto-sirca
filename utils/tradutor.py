# Mapeamento com base nas culturas comuns do dataset de recomendação agrícola
DICIONARIO_CULTURAS = {
    'rice': 'Arroz',
    'maize': 'Milho',
    'chickpea': 'Grão-de-bico',
    'kidneybeans': 'Feijão-de-corda',
    'pigeonpeas': 'Feijão-guandu',
    'mothbeans': 'Feijão-macaçar',
    'mungbean': 'Feijão-mungo',
    'blackgram': 'Feijão-da-índia',
    'lentil': 'Lentilha',
    'pomegranate': 'Romã',
    'banana': 'Banana',
    'mango': 'Manga',
    'grapes': 'Uva',
    'watermelon': 'Melancia',
    'muskmelon': 'Melão',
    'apple': 'Maçã',
    'orange': 'Laranja',
    'papaya': 'Mamão',
    'coconut': 'Coco',
    'cotton': 'Algodão',
    'jute': 'Juta',
    'coffee': 'Café'
}


def traduzir_cultura(nome_en):
    nome_limpo = str(nome_en).strip().lower()
    return DICIONARIO_CULTURAS.get(nome_limpo, nome_en.capitalize())
