
import os
import json
import requests
from time import sleep
from kafka import KafkaProducer


KAFKA_BROKER_URL = 'kafka:9092'

NOAA_TOKEN = os.environ.get('NOAA_TOKEN')
topic = 'weather_data'

producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER_URL,
                         value_serializer=lambda v: json.dumps(v).encode('utf'))


def fetch_weather_data():
    url = f'https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&locationid=FIPS:06&startdate=2024-03-01&enddate=2024-03-02&limit=5&datatypeid=TMAX&datatypeid=TMIN&units=metric'
    headers = {'token': NOAA_TOKEN}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data


if __name__ == '__main__':
    while True:
        weather_data = fetch_weather_data()
        producer.send(TOPIC, value=weather_data)
        print(f"Sent weather data to Kafka: {weather_data}")
        sleep(60)