from flask import Blueprint, render_template, request  # type: ignore
import joblib  # type: ignore
import pandas as pd  # type: ignore
import numpy as np  # type: ignore
import os
from utils.tradutor import traduzir_cultura
from utils.validacao import validar_dados_solo

recomendacao_bp = Blueprint('recomendacao', __name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_DIR = os.path.join(BASE_DIR, "sirca_model", "crop_model_save")

try:
    model = joblib.load(os.path.join(MODEL_DIR, "crop_recommendation_model.pkl"))
    crop_profiles = joblib.load(os.path.join(MODEL_DIR, "crop_profiles.pkl"))
    print("Sucesso: Artefatos do SIRCA carregados na Blueprint!")
except Exception as e:
    print(f"Erro ao carregar arquivos .pkl na rota: {e}")


@recomendacao_bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@recomendacao_bp.route('/predict', methods=['POST'])
def predict():
    try:
        features = {
            'N': float(request.form.get('N', 0)),
            'P': float(request.form.get('P', 0)),
            'K': float(request.form.get('K', 0)),
            'temperature': float(request.form.get('temperature', 0)),
            'humidity': float(request.form.get('humidity', 0)),
            'ph': float(request.form.get('ph', 0)),
            'rainfall': float(request.form.get('rainfall', 0))
        }

        valido, mensagem_erro = validar_dados_solo(features)
        if not valido:
            return render_template('index.html', erro=mensagem_erro, dados_enviados=features)

        input_df = pd.DataFrame([features])
        prediction_en = model.predict(input_df)[0]
        probabilities = model.predict_proba(input_df)[0]
        classes = model.classes_

        cultura_pt = traduzir_cultura(prediction_en)

        prob_map = sorted(list(zip(classes, probabilities)), key=lambda x: x[1], reverse=True)
        top_3 = []
        for i in range(min(3, len(prob_map))):
            top_3.append({
                'cultura': traduzir_cultura(prob_map[i][0]),
                'probabilidade': f"{prob_map[i][1] * 100:.2f}%"
            })

        confianca_principal = probabilities.max() * 100

        intervencoes = []
        valores_corrigidos = {}
        fator_critico = "Nenhum fator limitante crítico detectado."

        if prediction_en in crop_profiles.index:
            perfil_medio = crop_profiles.loc[prediction_en]
            desvios = []

            for col in features.keys():
                valores_corrigidos[col] = float(round(perfil_medio[col], 2))

                diff = perfil_medio[col] - features[col]
                limiar = 5.0 if col in ['N', 'P', 'K', 'temperature', 'rainfall'] else 0.5

                if abs(diff) > limiar:
                    sinal = "+" if diff > 0 else ""
                    intervencoes.append(f"Ajustar {col} em {sinal}{diff:.2f}")
                    desvios.append((col, abs(diff)))

            if desvios:
                fator_critico = "Níveis de nutrientes ou fatores climáticos distantes do padrão ideal recomendado."
        else:
            valores_corrigidos = features.copy()

        resultado = {
            'cultura': cultura_pt,
            'confianca': f"{confianca_principal:.2f}%",
            'top_3': top_3,
            'fator_limitante': fator_critico,
            'intervencoes': intervencoes,
            'adequacao_atual': f"{confianca_principal:.2f}%",
            'adequacao_potencial': f"{min(100.0, confianca_principal * 1.05):.2f}%",
            'valores_corrigidos': valores_corrigidos
        }

        return render_template('index.html', resultado=resultado, dados_enviados=features)

    except Exception as e:
        return render_template('index.html', erro=f"Erro interno de processamento: {str(e)}")


@recomendacao_bp.route('/sobre', methods=['GET'])
def sobre():
    return render_template('sobre.html')
