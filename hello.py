from flask import Flask, render_template, session, redirect, url_for, flash
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

__author__ = 'edfeng'

app = Flask(__name__)


class NameForm(Form):
    name = StringField("What's your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash("Looks like you've changed your name")
        session['name'] = form.name.data
        return redirect(url_for('index'))
    else:
        return render_template('index.html', form=form, name=session.get('name'))


if __name__ == '__main__':
    Bootstrap(app)
    app.config['SECRET_KEY'] = """3z&tlt+9_6cj+l69jnva(y*=7--2r)_j%kv6!+key6mb+6xxu5"""
    app.run(debug=True)
