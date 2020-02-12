# docker multistage builds
#https://github.com/psycopg/psycopg2/issues/684

FROM python:3.7-alpine
RUN apk add --no-cache python3-dev openssl-dev libffi-dev gcc musl-dev mariadb-dev && pip3 install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt
WORKDIR /code
COPY . .
CMD python manage.py run