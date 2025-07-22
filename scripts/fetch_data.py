import requests

URL = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
OUTPUT = "data/raw/covid_raw.csv"

def fetch_data():
    response = requests.get(URL)
    if response.status_code == 200:
        with open(OUTPUT, "wb") as f:
            f.write(response.content)
        print(" Data downloaded successfully.")
    else:
        print(" Failed to download data.")

if __name__ == "__main__":
    fetch_data()

