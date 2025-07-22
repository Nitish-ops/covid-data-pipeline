import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

DB = "db/covid.db"

def visualize():
    conn = sqlite3.connect(DB)
    query = """
        SELECT date, location, new_cases
        FROM covid_data
        WHERE location IN ('India', 'United States', 'Brazil')
    """
    df = pd.read_sql(query, conn, parse_dates=['date'])

    plt.figure(figsize=(12, 6))
    for country in df['location'].unique():
        country_df = df[df['location'] == country]
        plt.plot(country_df['date'], country_df['new_cases'], label=country)

    plt.title("Daily New COVID-19 Cases")
    plt.xlabel("Date")
    plt.ylabel("New Cases")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    visualize()
