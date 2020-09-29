# app/__init__.py
import os, time
from flask_restplus import Api
from flask import Blueprint

from .main.book.controller import api as book_controller

os.environ['TZ'] = 'America/Bogota'
time.tzset()

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Globant DevOps Academy',
          version='4.0'
        )


api.add_namespace(book_controller, path='/books')