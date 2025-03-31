# Базовый образ Python
FROM python:3.12

# Рабочая директория
WORKDIR /app

# Копируем зависимости и ставим их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь код
COPY . .

# Открываем порт и запускаем
EXPOSE 6080
CMD ["python", "main.py"]
