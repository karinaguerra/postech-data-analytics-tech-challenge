import time
import streamlit as st
import pandas as pd
from util.constantes import TITULO_PREV, TITULO_PRINCIPAL
from util.layout import output_layout

from util.load_data_limpo import main
import joblib
 # Importar as funções do seu módulo
from util.prophet_pipeline import limpar_df_ipea, realizar_previsao, plotar_previsao, calcular_metricas

st.set_page_config(
    page_title=f"{TITULO_PREV} | {TITULO_PRINCIPAL}",
    layout="wide",
)
output_layout()

with st.container():
    st.header(f"{TITULO_PREV}")


    st.write("""A Previsão de preços do petróleo Brent é um ponto importante para empresas no setor energético. Devido a ser um mercado com valores flutuantes e com impacto geopolíticos, as vezes os métodos tradicionais de previsão muitas vezes falham em capturar todas as variáveis envolvidas. Nesse contexto, modelos de predição baseados em machine learning têm se destacado como ferramentas poderosas para prever os preços do petróleo Brent. Para este estudo de caso, este são os resultados dos modelos escolhidos:""")


    tab0, tab1  = st.tabs(["Prophet", "LSTM (Long Short-Term Memory)"])
    
    with (tab0):
        # Carregar o modelo salvo
        @st.cache_resource
        def load_model():
            modelo = joblib.load('assets/modelos/prophet/modelo_prophet.pkl')
            return modelo

        modelo_prophet = load_model()

        st.write(':orange[Esta aplicação utiliza o modelo Prophet treinado para fazer previsões de até 90 dias]')

        # Entrada de dados pelo usuário
        periods = st.number_input('Insira o número de períodos para previsão:', min_value=1, max_value=90, value=30)

        freq = st.selectbox('Selecione a frequência da previsão:', ['Dias úteis (Business)','Diário', 'Semanal', 'Mensal'])

        # Mapeia a entrada de frequência para os valores usados pelo Prophet
        freq_dict = {
            'Dias úteis (Business)': 'B',
            'Diário': 'D',
            'Semanal': 'W',
            'Mensal': 'M'
        }
        freq_value = freq_dict[freq]

        if st.button('Prever'):
            with st.spinner("Carregando modelo ..."):
                time.sleep(3)
                previsao_prophet = realizar_previsao(modelo_prophet, periods=periods, freq=freq_value)

                # Plotar a previsão
                df_ipea = main()
                df_ipea = limpar_df_ipea(df_ipea)

                # Combinar previsões com dados reais para calcular métricas
                result = pd.merge(previsao_prophet[['ds', 'yhat']], df_ipea[['ds', 'y']], on='ds', how='inner')

                # Calcular métricas de desempenho
                mse, mae, r2, mape = calcular_metricas(result)

                st.caption("<small>:orange[Métricas de erro para o modelo Prophet]</small>", unsafe_allow_html=True)
                col1, col2, col3, col4 = st.columns(4)
                col1.metric('MSE', f'{mse:.2f}')
                col2.metric('MAE', f'{mae:.2f}')
                col3.metric('R²', f'{r2:.2f}')
                col4.metric('MAPE', f'{mape:.2f}%')
                st.write("---")


                fig = plotar_previsao(df_ipea, previsao_prophet)
                st.plotly_chart(fig)

                # Renomear colunas para exibição
                previsao_renomeada = result[['ds', 'y', 'yhat']].rename(columns={
                    'ds': 'Data',
                    'y': 'Valor Real',
                    'yhat': 'Previsão',
                })

                st.write(previsao_renomeada)
