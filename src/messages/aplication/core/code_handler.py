import datetime
import requests

class CodeHandler:
    def __init__(self):
        self.code_map = {
            1: self.handle_new_password,
            2: self.handle_new_login,
            3: self.handle_register,
            4: self.handle_delete_acc
        }
    
    def handle_code(self, code, ip=None, bill=None):
        if code in self.code_map:
            return self.code_map[code](ip, bill)
        else:
            return None

    def handle_new_password(self):
        subject = "Your password has been updated"
        body = f"To ensure the security of your account, please verify that you recently changed your password.\n\n"
        body += f"If you did not make this change, please contact our support team immediately.\n\n"
        body += f"Change made at: {datetime.datetime.now()}\n"
        return subject, body

    def handle_new_login(self, ip=None):
        location_data = self.get_location(ip)
        subject = "A new login session has occurred"
        body = f"A new login session has been detected for your account.\n\n"
        body += f"Login IP Address: {ip}\n"
        body += f"Location: {location_data['city']}, {location_data['region']}, {location_data['country']}\n\n"
        body += f"Login made at: {datetime.datetime.now()}\n"
        return subject, body
    
    def handle_register(self):
        subject = "Welcome to our platform!"
        body = f"Thank you for registering with us. We are excited to have you on board.\n\n"
        body += f"Please complete the registration process by following the instructions provided.\n\n"
        body += f"If you have any questions or need assistance, feel free to contact our support team.\n\n"
        body += f"Registration completed at: {datetime.datetime.now()}\n"
        return subject, body
    
    def handle_delete_acc(self):
        subject = "Account Deletion Confirmation"
        body = f"We regret to inform you that your account has been deleted.\n\n"
        body += f"If you did not initiate this action, please contact our support team immediately.\n\n"
        body += f"Account deleted at: {datetime.datetime.now()}\n"
        return subject, body
    
    def handle_new_bill(self, bill=None):
        subject = "New Bill Notification"
        concept = bill.get("concept")
        amount = bill.get("amount")

        body = f"We would like to inform you that a new bill has been generated.\n\n"
        body += f"Concept: {concept}\n"
        body += f"Amount: {amount}\n\n"
        body += f"Please review the bill details and make the payment by the due date.\n\n"
        body += f"If you have any questions or concerns regarding the bill, please contact our support team.\n\n"
        body += f"Bill generated at: {datetime.datetime.now()}\n"
    
        return subject, body
    
    def get_location(ip_address):
        response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
        location_data = {
            "ip": ip_address,
            "city": response.get("city"),
            "region": response.get("region"),
            "country": response.get("country_name")
        }
        return location_data
    