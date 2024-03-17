from python:3.9

WORKDIR /app

COPY requirements.txt /app/
RUN pip install poetry

COPY pyproject.toml poetry.lock* /app/

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

COPY . /app/

CMD ["python", "app.py"]