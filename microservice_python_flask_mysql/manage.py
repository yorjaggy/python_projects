import os
import unittest

from app import blueprint
from sqlalchemy import event
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app.main import create_app, db

app = create_app(os.getenv('EXAMPLE_ENV') or 'dev')
# Registering the flask app on blueprint
app.register_blueprint(blueprint)
app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@manager.command
def run():
    app.run(host='0.0.0.0')

if __name__ == '__main__':
    manager.run()
    