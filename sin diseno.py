from email.message import EmailMessage
import ssl
import smtplib
import os

email_sender = 'nicolascari.rz@gmail.com'
password = os.getenv('PASSWORD')

email_receiver = 'jose.sanchez.s@ucb.edu.bo'
subject = 'mr beast'
body = 'i want you for my 1 trillion subscriber video, click this link right now!!! virus.exe'

# SMTP server configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 465

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject

em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as smtp:
    smtp.login(email_sender, password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())


