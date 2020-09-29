#!/bin/bash
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
service nginx start
uwsgi --ini app.ini