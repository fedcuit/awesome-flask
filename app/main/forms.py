from wtforms import StringField, SubmitField
from flask.ext.wtf import Form
from wtforms.validators import DataRequired

__author__ = 'edfeng'


class NameForm(Form):
    name = StringField("What's your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")
