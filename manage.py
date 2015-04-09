#! /usr/bin/env python

__author__ = 'edfeng'

import os

from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand

print '{}: will package app get inited when import some definitions from it'.format(__name__)
import app as application
from app.models import User, Role

print '{}: inside module manage'.format(__name__)
print '{}: statements in module will be executed'.format(__name__)

region = os.environ.get('FLASK_CONFIG')
app = application.create_app(region)
manager = Manager(app)
migrate = Migrate(app, application.db)

print '{}: so you can see region now is evaluated with: {}'.format(__name__, region)


def make_shell_context():
    return dict(app=app, db=application.db, User=User, Role=Role)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)
if __name__ == '__main__':
    print "{}: while executing statements, found __name__ == '__main__' check, " \
          "it's still a statement, but only runs when this module is the main module, and now it's".format(__name__)
    # manager.run()
    app.run()