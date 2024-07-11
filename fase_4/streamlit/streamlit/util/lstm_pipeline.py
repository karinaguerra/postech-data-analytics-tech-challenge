# lstm_pipeline.py
import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
# from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential 
from tensorflow.keras.layers import LSTM, Dense
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

class DataCleaner(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X = X.copy()
        X.rename(columns={
            'Data': 'ds',
            'Preço - petróleo bruto - Brent (FOB)': 'y',
        }, inplace=True)
        X['ds'] = pd.to_datetime(X['ds'], format='%d/%m/%Y')
        X['y'] = X['y'].str.replace(',', '.').astype(float)
        X.sort_values(by=['ds'], ascending=True, inplace=True)
        X.set_index('ds', inplace=True)
        return X

class DataPreparer(BaseEstimator, TransformerMixin):
    def __init__(self, train_size=0.8):
        self.train_size = train_size
        self.scaler = MinMaxScaler(feature_range=(0, 1))
    
    def fit(self, X, y=None):
        close = X['y'].to_numpy().reshape(-1,1)
        train_close = int(len(close) * self.train_size)
        self.scaler.fit(close[0: train_close, :])
        return self
    
    def transform(self, X):
        close = X['y'].to_numpy().reshape(-1,1)
        train_close = int(len(close) * self.train_size)
        scaler_train = self.scaler.transform(close[0: train_close, :])
        scaler_test = self.scaler.transform(close[train_close:,:])
        
        scaled_data = list(scaler_train.reshape(len(scaler_train))) + list(scaler_test.reshape(len(scaler_test)))
        scaled_data = np.array(scaled_data).reshape(len(scaled_data),1)
        return scaled_data, train_close

class LSTMModel(BaseEstimator):
    def __init__(self, epochs=12, batch_size=32, scaler=None):
        self.epochs = epochs
        self.batch_size = batch_size
        self.model = None
        self.scaler = scaler
    
    def _create_model(self, input_shape):
        model = Sequential()
        model.add(LSTM(units=32, return_sequences=True, input_shape=input_shape))
        model.add(LSTM(units=32, return_sequences=True))
        model.add(LSTM(units=32))
        model.add(Dense(12))
        model.add(Dense(1))
        model.compile(optimizer='adam', loss='mean_squared_error')
        return model
    
    def fit(self, X, y=None):
        scaled_data, train_close = X
        train_data = scaled_data[0: train_close,:]
        
        X_train = []
        y_train = []
        for i in range(30, len(train_data)):
            X_train.append(train_data[i - 30:i, 0])
            y_train.append(train_data[i, 0])
        
        X_train, y_train = np.array(X_train), np.array(y_train)
        X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)
        
        self.model = self._create_model((X_train.shape[1], 1))
        self.model.fit(X_train, y_train, epochs=self.epochs, batch_size=self.batch_size)
        return self
    
    def predict(self, X):
        scaled_data, train_close = X
        test_data = scaled_data[train_close - 30:, :]
        
        X_test = []
        for i in range(30, len(test_data)):
            X_test.append(test_data[i - 30: i, 0])
        
        X_test = np.array(X_test)
        X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)
        
        prev_lstm = self.model.predict(X_test)
        prev_lstm = self.scaler.inverse_transform(prev_lstm)
        return prev_lstm

def avaliar_modelo(y_test, prev_lstm):
    mse = mean_squared_error(y_test, prev_lstm)
    mae = mean_absolute_error(y_test, prev_lstm)
    r2 = r2_score(y_test, prev_lstm)
    mape = np.mean(np.abs((y_test - prev_lstm) / y_test)) * 100
    return mse, mae, r2, mape