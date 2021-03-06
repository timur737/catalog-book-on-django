FROM python:3.8


RUN mkdir /code
WORKDIR /code

ADD . /code/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install -r requirements.txt

COPY . /code/


