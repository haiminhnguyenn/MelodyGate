from . import celery
from app.extensions import mail
from flask_mail import Message
from flask import render_template, current_app as app
import logging


logger = logging.getLogger(__name__)


@celery.task
def send_async_email(subject, recipients, body, html):
    message = Message(
        subject=subject,
        recipients=recipients,
        body=body,
        html=html
    )
    mail.send(message)
    logger.info("An email has been sent.")


def send_email(to, subject, template, **kwargs):
    subject_line = f"{app.config['MAIL_SUBJECT_PREFIX']} {subject}"
    body = render_template(f"{template}.txt", **kwargs)
    html = render_template(f"{template}.html", **kwargs)

    send_async_email.delay(subject_line, [to], body, html)