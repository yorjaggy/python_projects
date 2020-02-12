# app/__init__.py
import os, time
from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_controller

os.environ['TZ'] = 'America/Bogota'
time.tzset()

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='API Create and Request',
          version='1.0'
        )

api.add_namespace(user_controller, path='/user')

