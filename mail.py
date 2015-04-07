from threading import Thread

from flask import render_template
from flask.ext.mail import Message


__author__ = 'edfeng'


def compose_message(sender, to, subject, template, **kwargs):
    msg = Message(subject, sender=sender, recipients=[to],
                  body=render_template(template + '.txt', **kwargs), html=render_template(template + '.html', **kwargs))
    return msg


def send_mail(app, mail, msg):
    with app.app_context():
        mail.send(msg)


def async_send_mail(app, mail, sender, to, subject, template, **kwargs):
    msg = compose_message(sender, to, subject, template, **kwargs)
    t = Thread(target=send_mail, args=[app, mail, msg])
    t.start()
