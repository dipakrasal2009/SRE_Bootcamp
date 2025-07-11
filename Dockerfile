FROM python:3.10-slim AS base

WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
ENV PYTHONPATH=/app
#ENV PYTHONUNBUFFERED=1
CMD ["python", "app/main.py"]


