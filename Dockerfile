from python:3.12

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock* /app/
COPY README.md /app/

RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction --no-ansi

COPY . /app/

CMD ["python", "app.py"]