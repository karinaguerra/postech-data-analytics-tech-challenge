import streamlit as st
import joblib
import plotly.graph_objects as go
from util.load_data_limpo import main

# Importar as funções do seu módulo
from util.prophet_pipeline import limpar_df_ipea, realizar_previsao, plotar_previsao

# Carregar o modelo salvo
@st.cache_resource
def load_model():
    modelo = joblib.load('assets/modelos/prophet/modelo_prophet.pkl')
    return modelo

modelo_prophet = load_model()

st.title('App de Previsão com Prophet')

st.write('Este app utiliza um modelo Prophet treinado para fazer previsões.')

# Entrada de dados pelo usuário
periods = st.number_input('Insira o número de períodos para previsão:', min_value=1, max_value=90, value=30)
freq = st.selectbox('Selecione a frequência da previsão:', ['D', 'B', 'W', 'M'])

if st.button('Prever'):
    previsao_prophet = realizar_previsao(modelo_prophet, periods=periods, freq=freq)
    st.write(previsao_prophet[['ds', 'yhat', 'yhat_lower', 'yhat_upper']])

    # Plotar a previsão
    df_ipea = main()
    df_ipea = limpar_df_ipea(df_ipea)
    fig = plotar_previsao(df_ipea, previsao_prophet)
    st.plotly_chart(fig)
