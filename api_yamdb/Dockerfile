FROM python:3.7-slim

WORKDIR /app

RUN pip install --upgrade pip
COPY . .

WORKDIR /app/api_yamdb

RUN pip install -r requirements.txt --no-cache-dir

CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000"]
