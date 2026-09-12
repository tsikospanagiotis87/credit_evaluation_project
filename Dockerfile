FROM python:3.13-slim

WORKDIR /app

COPY Pipfile Pipfile.lock ./

RUN pip install pipenv
RUN pipenv install --system --deploy

COPY . .

CMD ["waitress-serve", "--listen=0.0.0.0:10000", "app:app"]
