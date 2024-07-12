import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from prophet import Prophet
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

import warnings
warnings.filterwarnings('ignore')

# Função para carregar dados
def carregar_dados(caminho):
    # Carregamento dos dado (load_data.py)
    return pd.read_csv(caminho, encoding='iso-8859-1', sep=';')

# Função para limpar dados
def limpar_dados(df):
    df.rename(columns={'Data': 'data', 'Preço - petróleo bruto - Brent (FOB)': 'valor'}, inplace=True)
    df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y')
    df['valor'] = df['valor'].str.replace(',', '.').astype(float)
    df.sort_values(by=['data'], ascending=True, inplace=True)
    return df

# Função para preparar dados para o Prophet
def preparar_dados(df, anos=4):
    df = df[df['data'] >= df['data'].max() - pd.DateOffset(years=anos)]
    df.rename(columns={'data': 'ds', 'valor': 'y'}, inplace=True)
    return df

# Função para dividir os dados em treino e teste
def dividir_dados(df, frac=0.8):
    train = df.sample(frac=frac, random_state=0)
    test = df.drop(train.index)
    return train, test

# Função para treinar e fazer previsões
def treinar_prever(train, periodos=120, freq='B'):
    modelo = Prophet(daily_seasonality=True)
    modelo.fit(train)
    future = modelo.make_future_dataframe(periods=periodos, freq=freq)
    previsoes = modelo.predict(future)
    return modelo, previsoes

# Função para avaliar as previsões
def avaliar_previsoes(train, previsoes):
    resultado = pd.merge(previsoes[['ds', 'yhat']], train[['ds', 'y']], on='ds', how='inner')
    y_true = resultado['y']
    y_pred = resultado['yhat']
    
    mse = mean_squared_error(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    mape = np.mean(np.abs((y_true - y_pred) / y_true)) * 100
    
    return mse, mae, r2, mape

# Função para plotar previsões
def plotar_previsoes(modelo, previsoes, train):
    plt.figure(figsize=(15, 8))
    
    # Plotando o treinamento e a previsão
    fig = modelo.plot(previsoes, ax=plt.gca(), figsize=(15, 8))
    
    # Adicionando o treinamento ao gráfico
    plt.plot(train['ds'], train['y'], 'o', markersize=4, color='orange')
    
    # Melhorias visuais
    plt.title('Previsão com Modelo Prophet', fontsize=18)
    plt.xlabel('Data', fontsize=14)
    plt.ylabel('Valor do Petróleo Brent', fontsize=14)

    # Melhorando a grade
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    
    # Ajustando os ticks dos eixos
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)

    # Tornando o fundo transparente
    fig.patch.set_alpha(0.0)  # Fundo da figura transparente
    plt.gca().patch.set_alpha(0.0)  # Fundo do eixo transparente
    
    plt.show()

# Atualizar o pipeline para incluir os dados de treinamento na função de plotar
def pipeline_prophet(caminho_dados):
    df = carregar_dados(caminho_dados)
    df_limpo = limpar_dados(df)
    df_prophet = preparar_dados(df_limpo)
    train, test = dividir_dados(df_prophet)
    
    modelo, previsoes = treinar_prever(train)
    mse, mae, r2, mape = avaliar_previsoes(train, previsoes)
    
    plotar_previsoes(modelo, previsoes, train)
    
    print(f'MSE: {mse:.2f}')
    print(f'MAE: {mae:.2f}')
    print(f'R²: {r2:.2f}')
    print(f'MAPE: {mape:.2f}%')


# Executar pipeline
caminho_dados = "C:/Users/KarinaNascimento1/Documents/05_Pessoal/02_Fiap/FASE4/fase_4/streamlit/data/ipeadata.csv"
