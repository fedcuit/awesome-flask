from flask import Blueprint

__author__ = 'edfeng'

main = Blueprint('main', __name__)
print "{}: i finally figure out the main package it used to hold 'main' blueprint and it's related view functions".format(
    __name__)
print "{}: inside main package, now main blueprint is initialized: {}".format(__name__, main)
print "{}: now going go register routes in views and errors to main blueprint".format(__name__)

print '{}: this import actually is used to bind view function to route'.format(__name__)
from . import views, errors