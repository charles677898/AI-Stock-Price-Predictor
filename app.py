from flask import (
    Flask,
    render_template,
    request,
    send_file
)

import yfinance as yf
import pandas as pd

from predictor import predict_stock

from database import (
    init_db,
    save_prediction,
    get_predictions,
    total_predictions,
    most_searched_stock,
    average_prediction,
    average_accuracy,
    export_csv
)

app = Flask(__name__)

# Create DB if not exists
init_db()


# ==========================
# HOME PAGE
# ==========================
@app.route("/")
def home():

    return render_template(
        "index.html"
    )


# ==========================
# PREDICT STOCK
# ==========================
@app.route("/predict", methods=["POST"])
def predict():

    symbol = request.form["symbol"].upper()

    try:

        prediction, accuracy = predict_stock(
            symbol
        )

        save_prediction(
            symbol,
            prediction,
            accuracy
        )

        return render_template(
            "index.html",
            symbol=symbol,
            prediction=prediction,
            accuracy=accuracy
        )

    except Exception as e:

        return render_template(
            "index.html",
            error=str(e)
        )


# ==========================
# HISTORY PAGE
# ==========================
@app.route("/history")
def history():

    data = get_predictions()

    return render_template(
        "history.html",
        data=data
    )


# ==========================
# DOWNLOAD CSV
# ==========================
@app.route("/download")
def download():

    file_path = export_csv()

    return send_file(
        file_path,
        as_attachment=True
    )


# ==========================
# DASHBOARD
# ==========================
@app.route("/dashboard")
def dashboard():

    total = total_predictions()

    searched = most_searched_stock()

    avg_prediction = average_prediction()

    avg_accuracy = average_accuracy()

    gainers, losers = get_market_movers()

    return render_template(
        "dashboard.html",
        total=total,
        searched=searched,
        avg_prediction=avg_prediction,
        avg_accuracy=avg_accuracy,
        gainers=gainers,
        losers=losers
    )


# ==========================
# TOP GAINERS / LOSERS
# ==========================
def get_market_movers():

    symbols = [
        "AAPL",
        "MSFT",
        "TSLA",
        "NVDA",
        "AMZN"
    ]

    results = []

    for symbol in symbols:

        try:

            stock = yf.download(
                symbol,
                period="5d",
                auto_adjust=True,
                progress=False
            )

            if stock.empty:
                continue

            if isinstance(
                stock.columns,
                pd.MultiIndex
            ):

                close_prices = stock[
                    ("Close", symbol)
                ]

            else:

                close_prices = stock[
                    "Close"
                ]

            latest = float(
                close_prices.iloc[-1]
            )

            previous = float(
                close_prices.iloc[-2]
            )

            change = round(
                (
                    (latest - previous)
                    / previous
                ) * 100,
                2
            )

            results.append(
                (
                    symbol,
                    change
                )
            )

        except:
            pass

    results.sort(
        key=lambda x: x[1],
        reverse=True
    )

    gainers = results[:3]

    losers = results[-3:]

    return gainers, losers


# ==========================
# RUN APP
# ==========================
if __name__ == "__main__":

    app.run(
        debug=True
    )