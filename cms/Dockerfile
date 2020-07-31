FROM python:3.8.5-buster

WORKDIR /code

RUN pip install pipenv
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
RUN pipenv install --system --dev

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]