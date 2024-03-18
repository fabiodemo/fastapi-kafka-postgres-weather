import json
import os
import requests
from time import sleep
from dotenv import load_dotenv

load_dotenv()

NOAA_TOKEN = os.environ.get('NOAA_TOKEN')
headers = {'token': NOAA_TOKEN}
print(NOAA_TOKEN)

def fetch_weather_data():
    url = f'https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&locationid=FIPS:06&startdate=2024-03-01&enddate=2024-03-02&limit=5&datatypeid=TMAX&datatypeid=TMIN&units=metric'
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        print(data)
        return data
    except requests.exceptions.HTTPError as http_err:
        print(f"Error in request: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Error in request: {req_err}")
    except ValueError:
        print(f"Invalid json")
    
    return {}

fetch_weather_data()