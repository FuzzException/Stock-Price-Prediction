import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_squared_error
from datetime import datetime
import plotly.graph_objects as go
import plotly.io as pio

def get_stock_data(symbol, start_date, end_date):
    stock_data = yf.download(symbol, start=start_date, end=end_date)
    return stock_data

def train_test_split(data, train_size):
    split_index = int(len(data) * train_size)
    train_data = data.iloc[:split_index]
    test_data = data.iloc[split_index:]
    return train_data, test_data

def evaluate_forecast(test_data, forecast):
    return mean_squared_error(test_data, forecast)

def plot_results(train_data, test_data, forecast1, forecast2, forecast_horizon):
    extended_test_data = pd.concat([test_data, pd.Series(index=pd.date_range(test_data.index[-1], periods=forecast_horizon))])

    today = datetime.today().strftime('%Y-%m-%d')
    extended_forecast1 = forecast1[:len(test_data) + (datetime.strptime(today, '%Y-%m-%d') - test_data.index[-1]).days]
    extended_forecast2 = forecast2[:len(test_data) + (datetime.strptime(today, '%Y-%m-%d') - test_data.index[-1]).days]

    trace1 = go.Scatter(x=train_data.index, y=train_data.values, mode='lines', name='Training Data', line=dict(color='blue'))
    trace2 = go.Scatter(x=extended_test_data.index, y=extended_test_data.values, mode='lines', name='Actual Stock Price', line=dict(color='green'))
    trace3 = go.Scatter(x=extended_test_data.index, y=extended_forecast1, mode='lines', name='ARIMA Forecast', line=dict(color='red'))
    trace4 = go.Scatter(x=extended_test_data.index, y=extended_forecast2, mode='lines', name='SARIMA Forecast', line=dict(color='orange'))

    layout = go.Layout(title='Stock Price Prediction',
                        xaxis=dict(title='Date'),
                        yaxis=dict(title='Stock Price'),
                        legend=dict(orientation="h"))

    fig = go.Figure(data=[trace1, trace2, trace3, trace4], layout=layout)
    
    # Save plot HTML file to static folder
    plot_path = 'static/plot.html'
    pio.write_html(fig, file=plot_path, auto_open=False)
    
    return plot_path

