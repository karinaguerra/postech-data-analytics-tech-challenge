import pandas as pd
from prophet import Prophet
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import plotly.graph_objects as go
import numpy as np 

def limpar_df_ipea(df_ipea):
    df_ipea.rename(columns={
        'Data': 'ds',
        'Preço - petróleo bruto - Brent (FOB)': 'y',
    }, inplace=True)
    df_ipea['ds'] = pd.to_datetime(df_ipea['ds'], format='%d/%m/%Y')
    df_ipea['y'] = df_ipea['y'].str.replace(',', '.').astype(float)
    df_ipea.sort_values(by=['ds'], ascending=True, inplace=True)
    return df_ipea

def treinar_modelo(train_data):
    model = Prophet(daily_seasonality=True)
    model.fit(train_data)
    return model

def realizar_previsao(model, periods=90, freq='B'):
    future = model.make_future_dataframe(periods=periods, freq=freq)
    forecast = model.predict(future)
    return forecast

def calcular_metricas(result):
    y_result = result['y']
    yhat_result = result['yhat']
    mse = mean_squared_error(y_result, yhat_result)
    mae = mean_absolute_error(y_result, yhat_result)
    r2 = r2_score(y_result, yhat_result)
    mape = (np.abs((y_result - yhat_result) / y_result)).mean() * 100
    return mse, mae, r2, mape