import sqlite3
import pandas as pd
import os

DB_DIR = "db"
DB = f"{DB_DIR}/covid.db"
INPUT = "data/processed/covid_cleaned.csv"

def load_data():
    # Ensure the db/ folder exists
    os.makedirs(DB_DIR, exist_ok=True)

    df = pd.read_csv(INPUT)

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS covid_data (
            location TEXT,
            date TEXT,
            new_cases REAL,
            total_cases REAL,
            new_deaths REAL,
            total_deaths REAL
        );
    """)

    df.to_sql('covid_data', conn, if_exists='replace', index=False)

    conn.commit()
    conn.close()
    print(" Data loaded into SQLite database.")

if __name__ == "__main__":
    load_data()
