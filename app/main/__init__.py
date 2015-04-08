from flask import Blueprint

__author__ = 'edfeng'

main = Blueprint('main', __name__)

from . import views, errors