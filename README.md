# SIRCA - Sistema de Recomendação de Culturas Agrícolas 🌾

O **SIRCA** é uma aplicação web desenvolvida para auxiliar produtores rurais e agrônomos na tomada de decisões agrícolas. Utilizando um modelo de Machine Learning, o sistema analisa as características químicas do solo e fatores climáticos para recomendar as três culturas agrícolas mais adequadas para o plantio, indicando também possíveis fatores limitantes.

## 🚀 Funcionalidades
* **Predição Inteligente:** Recomendação das 3 culturas mais aptas com base em IA[cite: 1].
* **Análise de Fatores Críticos:** Identificação automatizada caso os nutrientes ou clima estejam distantes do padrão ideal.
* **Interface Responsiva:** Design moderno e adaptados para uso em campo (desktop e mobile).

## 📊 Variáveis Analisadas pelo Modelo
* **N:** Teor de Nitrogênio no solo[cite: 1]
* **P:** Teor de Fósforo no solo[cite: 1]
* **K:** Teor de Potássio no solo[cite: 1]
* **Temperatura:** Temperatura ambiente em °C[cite: 1]
* **Umidade:** Umidade relativa do ar[cite: 1]
* **pH:** Acidez/alcalinidade do solo[cite: 1]
* **Precipitação:** Índice de chuvas em mm[cite: 1]

## 🛠️ Tecnologias Utilizadas
* **Backend:** Python (Flask)[cite: 1]
* **Machine Learning:** Scikit-Learn / Joblib (Modelos preditivos)[cite: 1]
* **Análise de Dados:** Pandas e NumPy[cite: 1]
* **Frontend:** HTML5, CSS3 (Customizado) e Jinja2[cite: 1]
* **Servidor de Produção:** Gunicorn[cite: 1]

## 💻 Como Rodar o Projeto Localmente

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/CristianoGO/projeto-sirca.git](https://github.com/CristianoGO/projeto-sirca.git)
   cd projeto-sirca
