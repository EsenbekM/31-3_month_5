FROM python:3.11

WORKDIR /app/

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /app/

RUN pip install -r /app/requirements.txt

COPY . /app/
