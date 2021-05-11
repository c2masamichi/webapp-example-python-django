FROM python:3.9.4-slim-buster

WORKDIR /code

RUN apt update \
  && apt install -y gcc default-libmysqlclient-dev
RUN pip install pipenv
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
RUN pipenv install --system --dev

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]