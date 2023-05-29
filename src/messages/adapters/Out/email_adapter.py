import smtplib
from email.message import EmailMessage
import ssl
from config.smtp_config import SMTPConfig

class EmailAdapter:
    def __init__(self):
        self.smtp_config = SMTPConfig()


    def send_email(self, sender, password, receiver, subject, body):
        em = EmailMessage()
        em['From'] = sender
        em['To'] = receiver
        em['Subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        try:
            with smtplib.SMTP_SSL(self.smtp_config.server, self.smtp_config.port, context=context) as smtp:
                smtp.login(sender, password)
                smtp.send_message(em)
            return 1
        except Exception as em:
            return 0
