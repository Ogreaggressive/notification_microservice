import datetime
import requests

class CodeHandler:
    def __init__(self):
        self.code_map = {
            1: self.handle_new_password,
            2: self.handle_new_login,
            3: self.handle_register,
            4: self.handle_delete_acc,
            5: self.handle_change_username,
            6: self.handle_new_bill
        }
    
    def handle_code(self, code, ip=None, bill=None, username=None):
        args = {'code':code,'ip':ip, 'bill':bill,'username':username}
        print(args)
        if code in self.code_map:
            subject,body = self.code_map[code](args)
            return subject,body
        else:
            return None

    def handle_new_password(self, args):
        subject = "Your password has been updated"
        body = f"To ensure the security of your account, please verify that you recently changed your password."
        body += f"If you did not make this change, please contact our support team immediately."
        body += f"Change made at: {datetime.datetime.now()}"
        return subject, body

    def handle_new_login(self, args):
        location_data = self.get_location(args["ip"])
        subject = "A new login session has occurred"
        body = f"A new login session has been detected for your account."
        body += f"Login IP Address: {args['ip']}"
        body += f"Location: {location_data['city']}, {location_data['region']}, {location_data['country']}"
        body += f" Login made at: {datetime.datetime.now()}"
        return subject, body

    def handle_register(self, args):
        subject = "Welcome to our platform!"
        body = f"Thank you for registering with us. We are excited to have you on board."
        body += f"Please complete the registration process by following the instructions provided."
        body += f"If you have any questions or need assistance, feel free to contact our support team."
        body += f"Registration completed at: {datetime.datetime.now()}"

        return subject, body

    def handle_delete_acc(self, args):
        subject = "Account Deletion Confirmation"
        body = f"We regret to inform you that your account has been deleted."
        body += f"If you did not initiate this action, please contact our support team immediately."
        body += f"Account deleted at: {datetime.datetime.now()}"
        return subject, body

    def handle_new_bill(self, args):
        subject = "New Bill Notification"
        concept = args["bill"].get("concept")
        amount = args["bill"].get("amount")

        body = f"We would like to inform you that a new bill has been generated."
        body += f"Concept: {concept}"
        body += f"Amount: {amount}"
        body += f"Please review the bill details and make the payment by the due date."
        body += f"If you have any questions or concerns regarding the bill, please contact our support team."
        body += f"Bill generated at: {datetime.datetime.now()}"

        return subject, body

    def get_location(self, ip_address):
        response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
        location_data = {
            "ip": ip_address,
            "city": response.get("city"),
            "region": response.get("region"),
            "country": response.get("country_name")
        }
        return location_data

    def handle_change_username(self, args):
        subject = "Username Change Confirmation"
        body = f"We would like to inform you that your account username has been changed."
        body += f"Your new username is: {args['username']}"
        body += f"If you did not initiate this change, please contact our support team immediately."
        body += f"Username changed at: {datetime.datetime.now()}"
        return subject, body