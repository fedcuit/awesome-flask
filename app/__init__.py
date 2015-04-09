from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.mail import Mail
from flask.ext.sqlalchemy import SQLAlchemy

print '{}: going to init package app'.format(__name__)
from config import config


__author__ = 'edfeng'

bootstrap = Bootstrap()
mail = Mail()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    bootstrap.init_app(app)
    mail.init_app(app)
    db.init_app(app)

    print "{} import main_blueprint which is defined in main package's init file".format(__name__)
    from .main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    return app