FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --default-timeout=100 --retries=10 --no-cache-dir -r requirements.txt

# Tüm proje
COPY . .

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app
