import sqlite3
import pandas as pd

DATABASE = "stock_data.db"


# Create Database
def init_db():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS predictions (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        stock_symbol TEXT NOT NULL,

        prediction REAL NOT NULL,

        accuracy REAL NOT NULL,

        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()

    conn.close()


# Save Prediction
def save_prediction(
    symbol,
    prediction,
    accuracy
):

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO predictions
    (
        stock_symbol,
        prediction,
        accuracy
    )
    VALUES (?, ?, ?)
    """,
    (
        symbol,
        prediction,
        accuracy
    ))

    conn.commit()

    conn.close()


# Prediction History
def get_predictions():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM predictions
    ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


# Dashboard Analytics
def total_predictions():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
    SELECT COUNT(*)
    FROM predictions
    """)

    total = cursor.fetchone()[0]

    conn.close()

    return total


def most_searched_stock():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
    SELECT stock_symbol,
           COUNT(*) AS total

    FROM predictions

    GROUP BY stock_symbol

    ORDER BY total DESC

    LIMIT 1
    """)

    result = cursor.fetchone()

    conn.close()

    if result:
        return result[0]

    return "N/A"


def average_prediction():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
    SELECT AVG(prediction)
    FROM predictions
    """)

    result = cursor.fetchone()[0]

    conn.close()

    if result:
        return round(result, 2)

    return 0


def average_accuracy():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
    SELECT AVG(accuracy)
    FROM predictions
    """)

    result = cursor.fetchone()[0]

    conn.close()

    if result:
        return round(result, 2)

    return 0


# Export CSV
def export_csv():

    conn = sqlite3.connect(DATABASE)

    df = pd.read_sql_query(
        "SELECT * FROM predictions",
        conn
    )

    file_name = "predictions.csv"

    df.to_csv(
        file_name,
        index=False
    )

    conn.close()

    return file_name