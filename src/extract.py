import requests
import pandas as pd

def extract_data():

    # API URL (public COVID data)
    url = "https://disease.sh/v3/covid-19/countries"

    # Request data from API
    response = requests.get(url, timeout=30)

    # Convert JSON to DataFrame
    df = pd.DataFrame(response.json())

    return df