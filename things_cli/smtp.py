import os
import smtplib
from contextlib import contextmanager

import click

from email.message import EmailMessage

FROM_EMAIL = os.environ.get('FROM_EMAIL')
FROM_EMAIL_PASSWORD = os.environ.get('FROM_EMAIL_PASSWORD')
TO_EMAIL = os.environ.get('TO_EMAIL')
SMTP_ADDRESS = os.environ.get('SMTP_ADDRESS')
SMTP_PORT = os.environ.get('SMTP_PORT')


def send_email_message(subject, body):
    """Sends email message via Google Mail SMTP."""
    if not any([FROM_EMAIL, FROM_EMAIL_PASSWORD, TO_EMAIL, SMTP_ADDRESS, SMTP_PORT]):
        raise ValueError(
            '''
            One of the variables -'
            'FROM_EMAIL, FROM_EMAIL_PASSWORD, TO_EMAIL, SMTP_ADDRESS, SMTP_PORT '
            'is missing in environment
            '''
        )

    message = EmailMessage()
    message['Subject'] = subject
    message['From'] = FROM_EMAIL
    message['To'] = TO_EMAIL
    message.set_content(body)

    with connect_to_server() as conn:
        if conn:
            conn.send_message(message)
            return True
    return False


@contextmanager
def connect_to_server():
    try:
        conn = smtplib.SMTP_SSL(SMTP_ADDRESS, SMTP_PORT)
        conn.ehlo()
        conn.login(FROM_EMAIL, FROM_EMAIL_PASSWORD)
        yield conn
    except Exception as e:
        click.echo('Error while sending email to {}: \n {}'.format(TO_EMAIL, e), err=True)
        yield False
    finally:
        if conn:
            conn.quit()
