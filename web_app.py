import os
import json
import psycopg2
from fastapi import FastAPI, HTTPException

app = FastAPI()

POSTGRES_HOST = os.environ.get('POSTGRES_HOST')
POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
POSTGRES_DB = os.environ.get('POSTGRES_DB')


@app.get('/')
def read_root():
    conn = psycopg2.connect(host=POSTGRES_HOST, user=POSTGRES_USER,
                            password=POSTGRES_PASSWORD, dbname=POSTGRES_DB)
    cur = conn.cursor()
    cur.execute("SELECT data FROM weather ORDER BY id DESC LIMIT 10")
    weather_data = [row[0] if isinstance(row[0], dict) else json.loads(row[0]) for row in cur.fetchall()]
    cur.close()
    conn.close()
    return {"weather_data": weather_data}
