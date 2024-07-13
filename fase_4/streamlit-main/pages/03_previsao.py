import time
import joblib
import numpy as np
import streamlit as st
import pandas as pd
from util.sidebar import sidebar_layout
from util.load_data_limpo import main
from util.prophet_pipeline import limpar_df_ipea, realizar_previsao, plotar_previsao, calcular_metricas
from util.lstm_pipeline import DataCleaner, DataPreparer, LSTMModel, avaliar_modelo
from keras.models import load_model
import plotly.graph_objects as go
from sklearn.preprocessing import StandardScaler

st.set_page_config(
    page_title=f"Previsão", layout="wide", initial_sidebar_state="expanded"
)
sidebar_layout()

with st.container():
    st.header(f"Previsão")

    st.write("""A Previsão de preços do petróleo Brent é um ponto importante para empresas no setor energético. Devido a ser um mercado com valores flutuantes e com impacto geopolíticos, as vezes os métodos tradicionais de previsão muitas vezes falham em capturar todas as variáveis envolvidas. Nesse contexto, modelos de predição baseados em machine learning têm se destacado como ferramentas poderosas para prever os preços do petróleo Brent. Para este estudo de caso, este são os resultados dos modelos escolhidos:""")

    tab0, tab1  = st.tabs(["Prophet", "LSTM (Long Short-Term Memory)"])
    
    with (tab0):
        # Carregar o modelo salvo
        @st.cache_resource
        def load_model():
            modelo = joblib.load('streamlit-main/modelos/modelo_prophet.pkl')
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

        if st.button('Executar Previsão', key='btn_prev_prophet' ):
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
    with (tab1):

        df_ipea_lstm = main()

        # Executar etapas individuais do pipeline
        data_cleaner = DataCleaner()
        df_ipea_lstm = data_cleaner.fit_transform(df_ipea_lstm)

        data_preparer = DataPreparer(train_size=0.8, scaler=StandardScaler())
        scaled_data, train_close = data_preparer.fit_transform(df_ipea_lstm)

        if st.button('Executar Previsão', key='btn_prev_lstm' ):
            with st.spinner("Carregando modelo ..."):
                time.sleep(3)

                lstm_model = LSTMModel(epochs=5, batch_size=50, scaler=data_preparer.scaler)
                lstm_model.fit((scaled_data, train_close))

                # Fazer previsões
                y_test = df_ipea_lstm['y'].values[train_close:]  # Use the original scale for y_test
                prev_lstm = lstm_model.predict((scaled_data, train_close))

                # Calcular métricas de desempenho
                mse, mae, r2, mape = avaliar_modelo(y_test, prev_lstm)

                st.caption("<small>:orange[Métricas de erro para o modelo Prophet]</small>", unsafe_allow_html=True)
                col1, col2, col3, col4 = st.columns(4)
                col1.metric('MSE', f'{mse:.2f}')
                col2.metric('MAE', f'{mae:.2f}')
                col3.metric('R²', f'{r2:.2f}')
                col4.metric('MAPE', f'{mape:.2f}%')
                st.write("---")

                # Prever futuro
                def prever_futuro(model, close, scaler):
                    last_30_days_scaled = scaler.transform(close[-30:].reshape(-1, 1))

                    X_test = np.array([last_30_days_scaled])
                    X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)

                    predictions = []
                    for i in range(30):
                        pred_future = model.predict(X_test)
                        predictions.append(pred_future)
                        X_test = np.append(X_test[:, 1:, :], pred_future.reshape(1, 1, 1), axis=1)

                    predictions = np.array(predictions).reshape(-1, 1)
                    predictions = scaler.inverse_transform(predictions)
                    return predictions


                # Prever futuro
                predictions = prever_futuro(lstm_model.model, df_ipea_lstm['y'].to_numpy(), data_preparer.scaler)
                # Filtrar os últimos 4 anos de dados
                ultima_data = df_ipea_lstm.index.max()
                quatro_anos_atras = ultima_data - pd.DateOffset(years=4)
                df_ipea_ultimos_4_anos = df_ipea_lstm[df_ipea_lstm.index >= quatro_anos_atras]
                # Preparar os dados de previsão
                proxima_data = ultima_data + pd.Timedelta(days=1)
                dates = pd.date_range(start=proxima_data, periods=30, freq='D')
                future_predictions_df = pd.DataFrame({'ds': dates, 'previsao': predictions.flatten()})
                future_predictions_df.set_index('ds', inplace=True)
                # Concatenar os dados reais filtrados com os dados de previsão
                combined_df = pd.concat([df_ipea_ultimos_4_anos, future_predictions_df])
                # Plotar os resultados
                fig = go.Figure()
                fig.add_trace(go.Scatter(x=df_ipea_ultimos_4_anos.index, y=df_ipea_ultimos_4_anos['y'], name='Valor Real', line=dict(color='steelblue')))
                fig.add_trace(go.Scatter(x=combined_df.index, y=combined_df['previsao'], name='Previsão', line=dict(color='orange')))
                fig.update_layout(
                    title='Previsão LSTM vs Valores Reais',
                    xaxis_title='Data',
                    yaxis_title='Valor',
                    legend_title='Tipo',
                    template='plotly_white'
                )
                st.plotly_chart(fig)

                future_predictions_df.reset_index(inplace=True)
                prev_renomeada = future_predictions_df.rename(columns={
                    'ds': 'Data',
                    'previsao': 'Previsão',
                })
                # Exibe a tabela no Streamlit
                st.write(prev_renomeada)