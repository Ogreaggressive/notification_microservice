from domain.models import EmailMessage
from domain.services import EmailService

class EmailController:
    def __init__(self, email_service: EmailService):
        self.email_service = email_service

    def send_email(self, sender, password, receiver, subject, body):
        email_message = EmailMessage(sender, receiver, subject, body)
        self.email_service.send_email(email_message)

