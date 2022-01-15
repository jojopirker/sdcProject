FROM python:3.8

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY /model /model

COPY app.py app.py

EXPOSE 8000

CMD uvicorn app:app --host 0.0.0.0 --root-path /api/
