#! /usr/bin/env python

__author__ = 'edfeng'

import os

from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand

import app as application
from app.models import User, Role

region = os.environ.get('FLASK_CONFIG')
app = application.create_app(region)
manager = Manager(app)
migrate = Migrate(app, application.db)


def make_shell_context():
    return dict(app=app, db=application.db, User=User, Role=Role)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)
if __name__ == '__main__':
    manager.run()