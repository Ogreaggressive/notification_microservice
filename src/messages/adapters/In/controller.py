# app/controllers/user_controller.py
from flask import Blueprint, request, jsonify
from domain.models import EmailMessage
from domain.services import EmailService
from aplication.core.code_handler import CodeHandler

messageBP = Blueprint('user', __name__)
code_handler = CodeHandler()

@messageBP.route('/send_mail/new_Login', methods=['POST'])
def send_new_login_mail():
    data = request.get_json()
    receiver_id = data["id"]
    ip = '114.124.155.43'
    subject,body = code_handler.handle_code(2, ip=ip)
    info = EmailMessage(receiver_id, subject, body)
    email_service = EmailService()
    email_service.send_email(info)

@messageBP.route('/send_mail/Register', methods=['POST'])
def send_new_login_mail():
    data = request.get_json()
    receiver_id = data["id"]
    subject,body = code_handler.handle_code(3)
    info = EmailMessage(receiver_id, subject, body)
    email_service = EmailService()
    email_service.send_email(info)

@messageBP.route('/send_mail/password_change', methods=['POST'])
def send_new_password_mail():
    data = request.get_json()
    receiver_id = data["id"]
    subject,body = code_handler.handle_code(1)
    info = EmailMessage(receiver_id, subject, body)
    email_service = EmailService()
    email_service.send_email(info)

@messageBP.route('/send_mail/user_deleted', methods=['POST'])
def send_new_password_mail():
    data = request.get_json()
    email = data["email"]
    subject,body = code_handler.handle_code(4)
    info = EmailMessage(receiver=email, subject=subject, body=body)
    email_service = EmailService()
    email_service.send_email(info)

@messageBP.route('/send_mail/new_bill_info', methods=['POST'])
def send_new_password_mail():
    data = request.get_json()
    email = data["id"]
    bill = {
    "concept": data["concept"],
    "amount": data["amount"],
    "date": data["date"]
    }
    subject, body = code_handler.handle_code(4, bill=bill)
    info = EmailMessage(receiver=email, subject=subject, body=body)
    email_service = EmailService()
    email_service.send_email(info)

    """
    if user:
        response = {
            'message': 'User created successfully',
            'userID': user.userID,
            'username': user.username,
            'email': user.email
        }
        return jsonify(response), 201
    else:
        return jsonify({'message': 'Failed to create user'}), 500"""
