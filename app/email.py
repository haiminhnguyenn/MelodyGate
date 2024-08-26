from . import celery
from app.extensions import mail
from flask_mail import Message
from flask import render_template, current_app as app
import logging

logger = logging.getLogger(__name__)

@celery.task
def send_async_email(message):
    mail.send(message)
    logger.info("An email has been sent.")
    

def send_email(to, subject, template, **kwargs):
    message = Message(
        subject=f"{app.config["MAIL_SUBJECT_PREFIX"]} {subject}",
        recipients=[to],
        body=render_template(f"{template}.txt", **kwargs),
        html=render_template(f"{template}.html", **kwargs)
    )
    
    send_async_email.delay(message)