FROM python:3.7-alpine
MAINTAINER Daniela Quesada T

ENV PYTHONUNBUFFERED 1

# DEPENDENCIES copy to docker image and store:
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

# creates a user for running applications only
# prevents root acces limiting scope 
RUN adduser -D user
USER user 
