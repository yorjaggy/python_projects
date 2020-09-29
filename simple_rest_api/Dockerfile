FROM python:3.7-slim
WORKDIR /code
RUN apt-get update
RUN apt-get install gcc g++  -y

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install --no-cache-dir uwsgi
RUN apt-get update
RUN apt-get install nginx -y
COPY nginx.conf /etc/nginx

EXPOSE 80 8312

COPY . .
RUN chmod +x ./start.sh

ENTRYPOINT ["./start.sh"]