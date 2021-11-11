FROM python:3.8
RUN pip install pipenv
RUN pipenv install django

# ENV PYTHONUNBUFFERED=1
# WORKDIR /app
# COPY Pipfile.lock Pipfile.lock
# RUN pip install pipenv
# RUN pipenv sync
