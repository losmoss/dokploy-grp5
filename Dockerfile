FROM python:3.11-slim

WORKDIR /app

COPY flask-app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY flask-app/app.py .

CMD ["python", "app.py"]
