from threading import Thread

from flask import render_template
from flask.ext.mail import Message

from app import mail
from manage import app


__author__ = 'edfeng'


def compose_message(sender, to, subject, template, **kwargs):
    msg = Message(subject, sender=sender, recipients=[to],
                  body=render_template(template + '.txt', **kwargs), html=render_template(template + '.html', **kwargs))
    return msg


def send_mail(msg):
    with app.app_context():
        mail.send(msg)


def async_send_mail(subject, template, **kwargs):
    msg = compose_message(app.config['MAIL_USERNAME'], app.config['ADMIN_EMAIL_ADDRESS'], subject, template, **kwargs)
    t = Thread(target=send_mail, args=[app, mail, msg])
    t.start()
