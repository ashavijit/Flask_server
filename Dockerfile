FROM python:3.8-slim

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "app.py"]


