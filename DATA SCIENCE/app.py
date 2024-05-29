from flask import Flask, render_template, request
from stock import get_stock_data, train_test_split, evaluate_forecast, plot_results
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    symbol = request.form['symbol']
    start_date = request.form['start_date']
    end_date = datetime.today().strftime('%Y-%m-%d')
    
    stock_data = get_stock_data(symbol, start_date, end_date)
    close_prices = stock_data['Close']
    train_data, test_data = train_test_split(close_prices, train_size=0.8)
    
    model1 = ARIMA(train_data, order=(5,1,0))
    model2 = SARIMAX(train_data, order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
    
    fitted_model1 = model1.fit()
    fitted_model2 = model2.fit()

    forecast1 = fitted_model1.forecast(steps=len(test_data))
    forecast2 = fitted_model2.forecast(steps=len(test_data))
    
    mse1 = evaluate_forecast(test_data, forecast1)
    mse2 = evaluate_forecast(test_data, forecast2)

    plot_path = plot_results(train_data, test_data, forecast1, forecast2, forecast_horizon=3)

    return render_template('results.html', symbol=symbol, mse1=mse1, mse2=mse2, plot_url=plot_path)

if __name__ == '__main__':
    app.run(debug=True,port = 8000)
