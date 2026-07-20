# SIRCA - Sistema de Recomendação de Culturas Agrícolas

O **SIRCA** é uma aplicação web desenvolvida para auxiliar produtores rurais e agrônomos na tomada de decisões agrícolas. Utilizando um modelo de Machine Learning, o sistema analisa as características químicas do solo e fatores climáticos para recomendar as três culturas agrícolas mais adequadas para o plantio, indicando também possíveis fatores limitantes.

## 🚀 Funcionalidades
* **Predição Inteligente:** Recomendação das 3 culturas mais aptas com base em IA[cite: 1].
* **Análise de Fatores Críticos:** Identificação automatizada caso os nutrientes ou clima estejam distantes do padrão ideal.
* **Interface Responsiva:** Design moderno e adaptados para uso em campo (desktop e mobile).

## 📊 Variáveis Analisadas pelo Modelo
* **N:** Teor de Nitrogênio no solo
* **P:** Teor de Fósforo no solo
* **K:** Teor de Potássio no solo
* **Temperatura:** Temperatura ambiente em °C
* **Umidade:** Umidade relativa do ar
* **pH:** Acidez/alcalinidade do solo
* **Precipitação:** Índice de chuvas em mm

## 🛠️ Tecnologias Utilizadas
* **Backend:** Python (Flask)
* **Machine Learning:** Scikit-Learn / Joblib (Modelos preditivos)
* **Análise de Dados:** Pandas e NumPy
* **Frontend:** HTML5, CSS3 (Customizado) e Jinja2
* **Servidor de Produção:** Gunicorn

## 📊 Aplicação web do SIRCA:
<img src="[URL_da_Imagem](https://github.com/CristianoGO/projeto-sirca/blob/main/imgs_sirca_app_web/01.png)" alt="Texto Alternativo" width="500">

## 📊 Recomendação:
<img src="[URL_da_Imagem](https://github.com/CristianoGO/projeto-sirca/blob/main/imgs_sirca_app_web/02.png)" alt="Texto Alternativo" width="500">

## 📊 Recomendação atualizada, com aplicação dos fatores limitantes nos dados inseridos no formulário:
<img src="[URL_da_Imagem](https://github.com/CristianoGO/projeto-sirca/blob/main/imgs_sirca_app_web/03.png)" alt="Texto Alternativo" width="500">

## 📊 Sobre o sistema:
<img src="[URL_da_Imagem](https://github.com/CristianoGO/projeto-sirca/blob/main/imgs_sirca_app_web/04.png)" alt="Texto Alternativo" width="500">

