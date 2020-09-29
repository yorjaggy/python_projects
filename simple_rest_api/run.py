import os

from app import blueprint
from app.main import create_app

application = create_app(os.getenv('EXEC_ENV') or 'dev')
application.register_blueprint(blueprint)
application.app_context().push()

if __name__ == '__main__':
    application.run()