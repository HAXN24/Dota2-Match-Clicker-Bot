import os
import smtplib
from email.message import EmailMessage
import ssl
from datetime import datetime

email_address = os.environ.get('myEmailAddress')
email_password = os.environ.get('myEmailPassword')
email_receiver = os.environ.get('emailReceiver')


def sendEmail():
    # Hiding sensitive information in environment variables
    email_address = os.environ.get('myEmailAddress')
    email_password = os.environ.get('myEmailPassword')

    # email body

    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    subject = 'Dota 2 Match Accepted! '
    body = f'A match has been accepted! {dt_string}'

    # email format
    emailMessage = EmailMessage()
    emailMessage['From'] = email_address
    emailMessage['To'] = email_receiver
    emailMessage['Subject'] = subject
    emailMessage.set_content(body)

    sslContext = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=sslContext) as smtp:
        smtp.login(email_address, email_password)
        smtp.sendmail(email_address, email_receiver, emailMessage.as_string())
