import os

basedir = os.path.abspath(os.path.dirname(__file__))


class DevelopmentConfig():
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://useracad:passacad@localhost/dbacad?charset=utf8mb4' if os.getenv('SQLALCHEMY_DATABASE_URI') == None else os.getenv('SQLALCHEMY_DATABASE_URI')


class TestingConfig():
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://useracad:passacad@mysqldb/dbacadtest?charset=utf8mb4' if os.getenv('SQLALCHEMY_DATABASE_URI') == None else os.getenv('SQLALCHEMY_DATABASE_URI')


class UserAceptanceTestingConfig():
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://useracad:passacad@mysqldb/dbacaduat?charset=utf8mb4' if os.getenv('SQLALCHEMY_DATABASE_URI') == None else os.getenv('SQLALCHEMY_DATABASE_URI')


class ProductionConfig():
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://useracad:passacad@mysqldb/dbacadprd?charset=utf8mb4' if os.getenv('SQLALCHEMY_DATABASE_URI') == None else os.getenv('SQLALCHEMY_DATABASE_URI')


config_by_name = dict(
    dev=DevelopmentConfig,
    qa=TestingConfig,
    uat = UserAceptanceTestingConfig,
    prod=ProductionConfig
)