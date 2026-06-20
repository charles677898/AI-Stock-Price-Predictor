import yfinance as yf
import pandas as pd
import numpy as np
import plotly.express as px

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score


def predict_stock(symbol):

    stock = yf.download(
        symbol,
        period="1y",
        auto_adjust=True,
        progress=False
    )

    if stock.empty:
        raise Exception("Invalid Stock Symbol")

    # Handle MultiIndex columns
    if isinstance(stock.columns, pd.MultiIndex):
        close_prices = stock[("Close", symbol)]
    else:
        close_prices = stock["Close"]

    df = pd.DataFrame(close_prices)

    df.columns = ["Close"]

    df["Prediction"] = df["Close"].shift(-1)

    df.dropna(inplace=True)

    X = df[["Close"]]

    y = df["Prediction"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = LinearRegression()

    model.fit(X_train, y_train)

    accuracy = r2_score(
        y_test,
        model.predict(X_test)
    )

    latest_close = np.array(
        [[df["Close"].iloc[-1]]]
    )

    prediction = model.predict(
        latest_close
    )

    create_stock_chart(df, symbol)

    create_prediction_chart(
        prediction[0],
        symbol
    )

    return (
        round(float(prediction[0]), 2),
        round(float(accuracy * 100), 2)
    )


def create_stock_chart(df, symbol):

    fig = px.line(
        df,
        x=df.index,
        y="Close",
        title=f"{symbol} Historical Prices"
    )

    fig.write_html(
        "static/stock_chart.html"
    )


def create_prediction_chart(prediction, symbol):

    days = [1, 2, 3, 4, 5]

    prices = [
        prediction,
        prediction + 1,
        prediction + 2,
        prediction + 3,
        prediction + 4
    ]

    future_df = pd.DataFrame({
        "Day": days,
        "Price": prices
    })

    fig = px.line(
        future_df,
        x="Day",
        y="Price",
        title=f"{symbol} Future Trend"
    )

    fig.write_html(
        "static/prediction_chart.html"
    )