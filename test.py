from smtplib import SMTP_SSL
import datetime
import time
import schedule
import requests

username = 'nikeadenike18@gmail.com'
password = 'adenike18'


def send_mail(text='Email Body', from_email='nikeadenike18@dmail.com', to_emails=[]):
    server = SMTP_SSL(host='smtp.gmail.com', port=465)
    server.login(username, password)
    server.sendmail(from_email, to_emails, text)
    server.quit()

send_mail(text='nikeadenike@gmail.com', to_emails=['nikeadenike@gmail.com','temitopeajagbe45@gmail.com'])

birthday = ["27/01/2021"]
receiver = ["nikeadenike@gmail.com", "temitopeajagbe45@gmail.com"]
schedule.every().birthday.at("8:00").do(send_mail)
