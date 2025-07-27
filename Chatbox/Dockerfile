FROM  python:3.11-slim-buster

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE

CMD ["uvicorn", "app.backend:app", "--host", "0.0.0.0", "--port", "10000"]