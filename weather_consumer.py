import os
import json
import psycopg2
from kafka import KafkaConsumer
import logging
logging.basicConfig(level=logging.DEBUG)


KAFKA_BROKER_URL = os.environ.get('KAFKA_BROKER_URL', 'kafka:29092')
POSTGRES_HOST = os.environ.get('POSTGRES_HOST')
POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
POSTGRES_DB = os.environ.get('POSTGRES_DB')

consumer = KafkaConsumer('weather_data', bootstrap_servers=KAFKA_BROKER_URL,
                         value_deserializer=lambda x: json.loads(x.decode('utf8')),
                         log_level='DEBUG'
                        )


def store_weather_data(weather_data):
    conn = psycopg2.connect(host=POSTGRES_HOST, user=POSTGRES_USER,
                            password=POSTGRES_PASSWORD, dbname=POSTGRES_DB)
    cur = conn.cursor()
    cur.execute("INSERT INTO weather (data) VALUES (%s)", (json.dumps(weather_data),))
    conn.commit()
    cur.close()
    conn.close()


if __name__ == '__main__':
    for message in consumer:
        weather_data = message.value
        store_weather_data(weather_data)
        print(f"Stored weather data in Postgres: {weather_data}")