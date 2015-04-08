from flask import session, redirect, url_for, render_template

from app import db
from app.email import async_send_mail
from app.main import main
from app.main.forms import NameForm
from app.models import User


__author__ = 'edfeng'


@main.route('/', methods=['GET', 'POST'])
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

