import logging
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv

load_dotenv()

email = os.getenv("gmail_user")
password = os.getenv("gmail_password")

logging.basicConfig()


class EmailService:

    @staticmethod
    def send_email(url):
        sender_email = email
        receiver_email = "abashlak@waverleysoftware.com"
        url_to_use = url

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = "Msg from CLI"
        body = "Check out this great new video: " + url_to_use
        body = MIMEText(body)
        msg.attach(body)

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            server.close()

            print('Email sent!')
        except Exception as e:
            logging.error('Failed.', exc_info=e)
            print('Something went wrong...')
