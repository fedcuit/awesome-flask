from flask import session, redirect, url_for, render_template

print '{} now inside views, try to import database from app package, ' \
      'will the init code in app package being run again'.format(__name__)
from app import db

from app.email import async_send_mail

print '{} try to import main_blueprint, will this results in circle dependency reference?'.format(__name__)
from app.main import main as main_blueprint

from app.main.forms import NameForm
from app.models import User


__author__ = 'edfeng'

print "{} I finally realize how route works, decorator itself is a function, " \
      "and when you put it above another function(let's say, view function), it will be invoked by python, passing the parameters" \
      "and included function, so it's a statement, this is now url are connected with view function"


@main_blueprint.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            async_send_mail('New Registration!', 'mail/new_registration', name=form.name.data)
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('.index'))
    else:
        return render_template('index.html', form=form, name=session.get('name'), known=session.get('known', False))

