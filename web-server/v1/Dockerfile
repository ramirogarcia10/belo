FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app
COPY app.py .

RUN pip install --no-cache-dir flask

USER nobody

EXPOSE 8080
CMD ["python", "app.py"]
