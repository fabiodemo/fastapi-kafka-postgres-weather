from python:3.11.7

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock* /app/
COPY README.md /app/
COPY weather_consumer.py weather_producer.py /app/
COPY wait-for-it.sh /wait-for-it.sh

RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction --no-ansi

COPY . /app/

CMD ["python", "app.py"]