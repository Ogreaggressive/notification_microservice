from domain.services import EmailService
from interfaces.controllers import EmailController

email_service = EmailService()
email_controller = EmailController(email_service)

sender='nicolascari.rz@gmail.com',
password='fkgwwgiqlcuwcwtx',

class Sender:
    def __init__(self):
        self.email_service=EmailService()
        self.email_controller = EmailController(email_service)
    
    def send_email(self, receiver, subject,body):
        self.email_controller.send_email(
            sender=sender,
            password=password,
            receiver=receiver,
            subject=subject,
            body=body
        )

sender = Sender()
receiver = 'christian.rivero@ucb.edu.bo'
subject = 'amogus'
body = 'no vuelvas a jugar los viernes bakaa onchias'

sender.send_email(receiver, subject, body)