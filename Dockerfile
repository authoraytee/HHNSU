
FROM python:3.8-slim-buster

WORKDIR /core

COPY . .
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile

