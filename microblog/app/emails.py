from .decorators import async

from flask import render_template
from flask_mail import Message

from app import mail, app
from config import ADMINS

@async
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    send_async_email(app, msg)

def follower_notification(follwed, follower):
    send_email(f'[microblog] {follower.nickname} is now following you!',
    ADMINS[0],
    [follwed.email],
    render_template('follower_email.txt',
    user=follwed, follower=follower),
    render_template('follower_email.html',
    user=follwed,follower=follower))
