# syntax=docker/dockerfile:1
FROM python:3.9 as base

WORKDIR /chatsky_pipeline

COPY requirements.txt requirements.txt
RUN ["python", "-m", "pip", "install", "-r", "requirements.txt"]

COPY bot ./bot
COPY __init__.py .
COPY test.py .
COPY test_data.json .
COPY test.sh .
COPY time_test.sh .

CMD exit 0
