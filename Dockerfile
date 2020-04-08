FROM python:3.7.6-slim

RUN apt-get update && apt-get install -y git

ENV PYTHONUNBUFFERED 1

WORKDIR /code
COPY ./requirements.txt /code

RUN pip install -r requirements.txt --src /usr/local/src
