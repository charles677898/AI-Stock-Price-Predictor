# 📈 Stock Price Predictor using Machine Learning

## Overview

Stock Price Predictor is a Python-based Machine Learning web application that predicts future stock prices using historical market data. The application fetches real-time stock data from Yahoo Finance, trains a Linear Regression model, and provides stock price predictions along with performance analytics.

The project also includes interactive charts, prediction history tracking, CSV export functionality, and an analytics dashboard.

---

## Features

* Predict stock prices using Machine Learning
* Real-time stock data from Yahoo Finance
* Model accuracy calculation
* Interactive historical stock price graphs
* Future prediction trend visualization
* SQLite database integration
* Prediction history tracking
* CSV export functionality
* Analytics dashboard
* Top Gainers and Top Losers analysis
* Responsive web interface using Flask

---

## Technologies Used

### Backend

* Python
* Flask
* SQLite

### Machine Learning

* Scikit-Learn
* Linear Regression

### Data Processing

* Pandas
* NumPy

### Visualization

* Plotly

### Stock Market Data

* Yahoo Finance (yfinance)

---

## Project Structure

```text
Stock-Price-Predictor/

│
├── app.py
├── predictor.py
├── database.py
├── requirements.txt
├── README.md
├── stock_data.db
│
├── templates/
│   ├── index.html
│   ├── history.html
│   └── dashboard.html
│
├── static/
│   ├── style.css
│   ├── script.js
│   ├── stock_chart.html
│   └── prediction_chart.html
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/Stock-Price-Predictor.git
cd Stock-Price-Predictor
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Project

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## Dashboard Features

* Total Predictions
* Most Searched Stock
* Average Prediction
* Average Accuracy
* Top Gainers
* Top Losers

---

## Future Enhancements

* LSTM Deep Learning Model
* Multi-stock comparison
* User authentication
* Cloud deployment
* Portfolio management
* Email alerts
* Real-time prediction updates

---

## Learning Outcomes

This project demonstrates:

* Machine Learning Fundamentals
* Data Analysis
* Flask Web Development
* Database Integration
* Data Visualization
* Financial Data Processing
* Software Development Best Practices

---

## Author

**Your Name**

Python Developer | Machine Learning Enthusiast

---

## License

This project is developed for educational and portfolio purposes.
