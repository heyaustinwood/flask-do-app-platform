import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    MAIL_USE_SSL = True

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/doappplatform'