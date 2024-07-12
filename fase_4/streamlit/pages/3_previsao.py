import pandas as pd
import numpy as np
import streamlit as st
import plotly.graph_objs as go
# from util.lstm_pipeline import DataCleaner, DataPreparer, LSTMModel, avaliar_modelo
from util.prophet_pipeline import limpar_df_ipea, treinar_modelo, realizar_previsao, calcular_metricas
from util.load_data import main
import time
from st_pages import show_pages_from_config

show_pages_from_config("config/pages_sections.toml")
# Titulo Pagina 
# st.set_page_config(layout='centered', 
#                    page_title="Previsão")

# Autor 
with st.sidebar:
    st.caption("<small>:orange[Criado por:]</small>", unsafe_allow_html=True)
    st.write("Karina Guerra do Nacimento")
    st.write("RM 352525")

# Titulo e subtitulo
with st.container():
    st.title("Previsão")
    st.write("""A Previsão de preços do petróleo Brent é um ponto importante para empresas no setor energético. Devido a ser um mercado com valores flutuantes e com impacto geopolíticos, as vezes os métodos tradicionais de previsão muitas vezes falham em capturar todas as variáveis envolvidas. Nesse contexto, modelos de predição baseados em machine learning têm se destacado como ferramentas poderosas para prever os preços do petróleo Brent. Para este estudo de caso, este são os resultados dos modelos escolhidos:""")


with st.container():
    st.write("---")
    st.write("Prophet")

    # Carregar dados
    df_ipea_prophet = main()
    # Limpar dados
    df_ipea_prophet = limpar_df_ipea(df_ipea_prophet)

    # Filtrar os últimos 4 anos de dados
    prophet_df_ipea = df_ipea_prophet[df_ipea_prophet['ds'] >= df_ipea_prophet['ds'].max() - pd.DateOffset(years=4)]
    # Dividir dados em treino e teste
    train_ipea = prophet_df_ipea.sample(frac=0.8, random_state=0)
    test_ipea = prophet_df_ipea.drop(train_ipea.index)

    # Instanciar e treinar o modelo Prophet
    modelo_prophet = treinar_modelo(train_ipea)

    # Realizar a previsão
    previsao_prophet = realizar_previsao(modelo_prophet)

    # Combinar previsões com dados reais para calcular métricas
    result = pd.merge(previsao_prophet[['ds', 'yhat']], train_ipea[['ds', 'y']], on='ds', how='inner')

    if st.button('Executar Previsão', key='btn_prev_prophet'):
         with st.spinner("Carregando modelo ..."):
            time.sleep(3)
               
         # Calcular métricas de desempenho
         mse, mae, r2, mape = calcular_metricas(result)
         st.caption("<small>:orange[Métricas de erro para o modelo Prophet]</small>", unsafe_allow_html=True)
         col1, col2, col3, col4 = st.columns(4)
         col1.metric('MSE', f'{mse:.2f}')
         col2.metric('MAE', f'{mae:.2f}')
         col3.metric('R²', f'{r2:.2f}')
         col4.metric('MAPE', f'{mape:.2f}%')
         st.write("---")

         # Plotly gráfico interativo
         fig = go.Figure()
         # Dados reais
         fig.add_trace(go.Scatter(x=prophet_df_ipea['ds'], y=prophet_df_ipea['y'], mode='lines', name='Dados Reais', line=dict(color='steelblue')))
         # Previsões
         fig.add_trace(go.Scatter(x=previsao_prophet['ds'], y=previsao_prophet['yhat'], mode='lines', name='Previsão', line=dict(color='orange')))
         fig.update_layout(title='Previsão de Preços do Petróleo', xaxis_title='Data', yaxis_title='Preço (Brent FOB)', legend=dict(x=0, y=1))
         st.plotly_chart(fig)