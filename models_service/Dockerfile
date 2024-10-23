# syntax=docker/dockerfile:1
FROM python:3.9 as base

WORKDIR /service

COPY requirements.txt requirements.txt
RUN ["python", "-m", "pip", "install", "-r", "requirements.txt"]

# cache mfaq model
RUN ["python3", "-c", "from sentence_transformers import SentenceTransformer; _ = SentenceTransformer('clips/mfaq')"]

COPY app.py .
COPY models ./models

CMD ["python", "app.py"]