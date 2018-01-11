import os
import smtplib
from contextlib import contextmanager
from email.message import EmailMessage

FROM_EMAIL = os.environ.get('FROM_EMAIL')
FROM_EMAIL_PASSWORD = os.environ.get('FROM_EMAIL_PASSWORD')
TO_EMAIL = os.environ.get('TO_EMAIL')
SMTP_ADDRESS = os.environ.get('SMTP_ADDRESS')
SMTP_PORT = os.environ.get('SMTP_PORT')
SMTP_LOGIN = os.environ.get('SMTP_LOGIN')
SMTP_PASSWORD = os.environ.get('SMTP_PASSWORD')


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

    with connect_to_server() as (conn, msg):
        if conn:
            conn.sendmail(FROM_EMAIL, TO_EMAIL, message.as_string())
            return True
    return msg


@contextmanager
def connect_to_server():
    try:
        conn = smtplib.SMTP(SMTP_ADDRESS, SMTP_PORT)
        conn.ehlo()
        conn.starttls()
        conn.ehlo()
        conn.login(SMTP_LOGIN, SMTP_PASSWORD)
        yield conn, ''
    except Exception as e:
        yield False, e
    finally:
        if conn:
            conn.close()
