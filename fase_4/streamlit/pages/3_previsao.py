import pandas as pd
import numpy as np
import streamlit as st
import plotly.graph_objs as go
from util.lstm_pipeline import DataCleaner, DataPreparer, LSTMModel, avaliar_modelo
from util.prophet_pipeline import limpar_df_ipea, treinar_modelo, realizar_previsao, calcular_metricas, plotar_previsao
from util.load_data import main
import time
from st_pages import show_pages_from_config

show_pages_from_config(".streamlit/pages_sections.toml")
# Titulo Pagina 
st.set_page_config(layout='centered', 
                   page_title="Previsão")

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
    tab0, tab1  = st.tabs(["Prophet", "LSTM (Long Short-Term Memory)"])

    # Conteúdo da aba "Prophet"
    with tab0:

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

    # Conteúdo da aba "LSTM"
    with tab1:

        # Carregar dados
        df_ipea_lstm = main()

        # Adicionar botão para executar as previsões
        if st.button('Executar Previsão', key="btn_prev_lstm"):
            with st.spinner("Carregando modelo ..."):
                time.sleep(3)

                # Executar etapas individuais do pipeline
                data_cleaner = DataCleaner()
                df_ipea_lstm = data_cleaner.fit_transform(df_ipea_lstm)

                data_preparer = DataPreparer()
                scaled_data, train_close = data_preparer.fit_transform(df_ipea_lstm)

                lstm_model = LSTMModel(epochs=10, batch_size=30, scaler=data_preparer.scaler)
                lstm_model.fit((scaled_data, train_close))

                # Fazer previsões
                y_test = df_ipea_lstm['y'].values[train_close:]  # Use the original scale for y_test
                prev_lstm = lstm_model.predict((scaled_data, train_close))

                st.caption("<small>:orange[Métricas de erro para o modelo LSTM]</small>", unsafe_allow_html=True)
                
                # Avaliar o modelo
                mse, mae, r2, mape = avaliar_modelo(y_test, prev_lstm)
                col1, col2, col3, col4= st.columns(4)
                col1.metric("MSE", f"{mse:.2f}")
                col2.metric("MAE", f"{mae:.2f}")
                col3.metric("R²", f"{r2:.2f}")
                col4.metric("MAPE", f"{mape:.2f}")
                st.write("---")

                # Prever futuro
                def prever_futuro(model, close, scaler):
                    X_test = np.array([scaler.transform(close[-30:].reshape(-1, 1))])
                    X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)
                    
                    predictions = []
                    for i in range(30):
                        pred_future = model.predict(X_test)
                        predictions.append(pred_future)
                        X_test = np.append(X_test[:, 1:, :], pred_future.reshape(1, 1, 1), axis=1)
                    
                    predictions = np.array(predictions).reshape(-1, 1)
                    predictions = scaler.inverse_transform(predictions)
                    return predictions

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