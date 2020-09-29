import os
from app import blueprint
from sqlalchemy import event
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app.main import create_app, db

application = create_app(os.getenv('EXEC_ENV') or 'dev')

application.register_blueprint(blueprint)
application.app_context().push()

manager = Manager(application)
migrate = Migrate(application, db)

manager.add_command('db', MigrateCommand)

@manager.command
def run():
    application.run(host='0.0.0.0', port=1080)


if __name__ == '__main__':
    manager.run()
    