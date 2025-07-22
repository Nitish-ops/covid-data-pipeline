import pandas as pd
import os

INPUT = "data/raw/covid_raw.csv"
OUTPUT_DIR = "data/processed"
OUTPUT = f"{OUTPUT_DIR}/covid_cleaned.csv"

def clean_data():
    df = pd.read_csv(INPUT)

    df = df[['location', 'date', 'new_cases', 'total_cases', 'new_deaths', 'total_deaths']]
    df = df[df['location'].isin(['India', 'United States', 'Brazil'])]

    df['date'] = pd.to_datetime(df['date'])
    df.fillna(0, inplace=True)

    # Create folder if not exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    df.to_csv(OUTPUT, index=False)
    print(" Data cleaned and saved.")

if __name__ == "__main__":
    clean_data()
