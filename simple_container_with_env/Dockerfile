FROM python:3.13-slim

WORKDIR /app

COPY app.py .

# Устанавливаем дефолтные значения переменных окружения
ENV DB_HOST=localhost
ENV DB_NAME=default_db
ENV DB_PORT=5432
ENV DB_USER=admin

CMD ["python", "app.py"]