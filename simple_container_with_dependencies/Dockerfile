FROM python:3.13-slim

WORKDIR /app

# Копируем requirements.txt первым (для кеширования слоя)
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Копируем код приложения
COPY app.py .

CMD ["python", "app.py"]