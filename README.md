# Stock-Price-Prediction
Real Time Stock Price Prediction using Time Series Forecasting : SARIMA Model and ARIMA Model 
<img width="1440" alt="stockpricepred1" src="https://github.com/FuzzException/Stock-Price-Prediction/assets/98276556/9558111c-c01d-44c9-ad57-3a39d950b2d3">
<img width="1440" alt="stockpricepred2" src="https://github.com/FuzzException/Stock-Price-Prediction/assets/98276556/0809237d-cdd0-4c78-bdc5-47fe67d65ea6">
<img width="1440" alt="stockpricepred3" src="https://github.com/FuzzException/Stock-Price-Prediction/assets/98276556/9a6baa7f-3c66-4420-aa89-b2015c31b985">


Stock Price Prediction Web Application

This project is a web application designed to predict stock prices using historical data and advanced time series forecasting techniques. Users can input a stock ticker symbol and date range, and the application will fetch historical stock prices, split the data into training and testing sets, apply forecasting models, evaluate their performance, and display the results.

#### Techniques and Technologies Used:

1. **Data Fetching**:
   - **yfinance**: Used to download historical stock price data.

2. **Data Processing**:
   - **pandas**: For data manipulation and handling time series data.
   - **NumPy**: For numerical operations and data handling.

3. **Forecasting Models**:
   - **ARIMA (AutoRegressive Integrated Moving Average)**: A popular time series forecasting method used to analyze and predict future points in the series.
   - **SARIMA (Seasonal ARIMA)**: Extends ARIMA by considering seasonal effects, providing more accurate forecasts for data with seasonality.

4. **Model Evaluation**:
   - **Mean Squared Error (MSE)**: Used to evaluate the accuracy of the forecasting models.

5. **Visualization**:
   - **matplotlib**: For initial plotting during development (replaced by Plotly for interactive plots).
   - **Plotly**: For creating interactive, web-based plots that are embedded in the web application.
   - **plotly.graph_objects**: Used to construct and customize the interactive plots.

6. **Web Framework**:
   - **Flask**: A lightweight web framework used to build the web application, handle user inputs, and render HTML templates.

7. **HTML and CSS**:
   - **HTML**: For structuring the web pages.
   - **CSS**: For styling the web pages and enhancing the user interface.

8. **JavaScript**:
   - Used to handle dynamic behavior on the client side, though minimal in this specific project setup.

### Workflow:

1. **User Input**:
   - Users input the stock ticker symbol and start date via an HTML form on the `index.html` page.

2. **Data Retrieval and Processing**:
   - The application fetches the historical stock data using yfinance.
   - Data is split into training and testing sets.

3. **Model Training and Forecasting**:
   - ARIMA and SARIMA models are trained on the training data.
   - Both models generate forecasts for the test data period.

4. **Evaluation and Visualization**:
   - The models' performances are evaluated using MSE.
   - Results and forecasts are plotted using Plotly and saved as an HTML file.

5. **Displaying Results**:
   - The results, including evaluation metrics and the interactive plot, are displayed on the `results.html` page.

This project demonstrates the integration of various data science and web development technologies to create a user-friendly application for stock price prediction.
