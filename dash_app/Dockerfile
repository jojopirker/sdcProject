FROM python:3.8

#Arguments for data download from kaggle
ARG kaggle_user
ARG kaggle_token

RUN pip install kaggle

ENV KAGGLE_USERNAME=$kaggle_user
ENV KAGGLE_KEY=$kaggle_token

# Data download and unzip
WORKDIR /data
RUN kaggle datasets download benoit72/uk-accidents-10-years-history-with-many-variables
RUN unzip uk-accidents-10-years-history-with-many-variables.zip

WORKDIR /app
# pip packages
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

# app
COPY app.py app.py

EXPOSE 8000
# app is hosted via uvicorn, note app is the file name and server the object
# forwarded_allow-ips is potentially dangerous, but behind azures firewall it hopefully is safe
CMD gunicorn app:server --bind 0.0.0.0:8000 --timeout 300 --forwarded-allow-ips '*' --log-level 'debug'