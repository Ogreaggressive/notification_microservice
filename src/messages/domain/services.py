from domain.models import EmailMessage
from adapters.Out.user_admin_adapter import user_admin_adapter
from adapters.Out.email_adapter import EmailAdapter
from adapters.Out.user_auth_adapter import user_auth_adapter
import os

class EmailService:
    def __init__(self):
        self.email_adapter = EmailAdapter()
        self.user_admin_adapter = user_admin_adapter()
        self.user_auth_adapter = user_auth_adapter()
        self.sender='nicolascari.rz@gmail.com'
        self.password = os.getenv('PASSWORD')


    def retrieve_user_email(self,id):
        return self.user_admin_adapter.get_email(id)
    
    def new_user_register(self):
        return self.user_auth_adapter.get_id_registering()
    
    def new_login_location(self):
            return self.user_auth_adapter.get_id_logging_in()

    def send_email(self, email_message: EmailMessage):
        if not email_message.receiverId:
            email_message.receiver = self.retrieve_user_email(email_message.receiverId)   
        self.email_adapter.send_email(
            sender=self.sender,
            password=self.password,
            receiver=email_message.receiver,
            subject=email_message.subject,
            body=email_message.body
        )