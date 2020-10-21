from flask_mail import Message
from youtube_mp3_site import mail
from flask import url_for, current_app
from youtube_mp3_site.config import Config

def send_issue_email(user, body):
    msg = Message('Issue with download',
            sender=user.data,
            recipients=[Config.MAIL_USERNAME], 
            body = f"Sent from: {user.data}\n{body.data}")

    mail.send(msg)