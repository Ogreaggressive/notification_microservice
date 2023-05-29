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
    receiver_id = data["userID"]
    ip = '114.124.155.43'
    subject,body = code_handler.handle_code(2, ip=ip)
    info = EmailMessage(receiverId=receiver_id,subject=subject,body=body)
    email_service = EmailService()
    email_sent = email_service.send_email(info)
    if email_sent == 1:
        response = {
            'message':'done'
        }
        return jsonify(response), 200
    else:
        return jsonify({'message': 'couldnt send'}), 404
    

@messageBP.route('/send_mail/Register', methods=['POST'])
def send_Register():
    data = request.get_json()
    receiver_id = data["id"]
    subject,body = code_handler.handle_code(3)
    info = EmailMessage(receiverId=receiver_id,subject=subject,body=body)
    email_service = EmailService()
    print(info.receiverId,info.body)
    email_sent = email_service.send_email(info)
    if email_sent == 1:
        response = {
            'message':'done'
        }
        return jsonify(response), 200
    else:
        return jsonify({'message': 'couldnt send'}), 404

@messageBP.route('/send_mail/password_change', methods=['PUT'])
def send_password_change():
    data = request.get_json()
    receiver_id = data["userID"] 
    subject,body = code_handler.handle_code(1)
    info = EmailMessage(receiverId=receiver_id,subject=subject,body=body)
    email_service = EmailService()
    email_sent = email_service.send_email(info)
    if email_sent == 1:
        response = {
            'message':'done'
        }
        return jsonify(response), 200
    else:
        return jsonify({'message': 'couldnt send'}), 404

@messageBP.route('/send_mail/user_deleted', methods=['POST'])
def send_user_deleted():
    data = request.get_json()
    email = data["email"]
    subject,body = code_handler.handle_code(4)
    info = EmailMessage(receiver=email, subject=subject, body=body)
    email_service = EmailService()
    email_sent = email_service.send_email(info)
    if email_sent == 1:
        response = {
            'message':'done'
        }
        return jsonify(response), 200
    else:
        return jsonify({'message': 'couldnt send'}), 404

@messageBP.route('/send_mail/change_username', methods=['POST'])
def send_change_username():
    data = request.get_json()
    receiver_id = data["userID"] 
    newUsername = data["newUsername"]
    subject,body = code_handler.handle_code(5,username=newUsername)
    info = EmailMessage(receiverId=receiver_id, subject=subject, body=body)
    email_service = EmailService()
    email_sent = email_service.send_email(info)
    if email_sent == 1:
        response = {
            'message':'done'
        }
        return jsonify(response), 200
    else:
        return jsonify({'message': 'couldnt send'}), 404

@messageBP.route('/send_mail/new_bill_info', methods=['POST'])
def send_billing_info():
    data = request.get_json()
    email = data["userID"]
    bill = {
    "concept": data["concept"],
    "amount": data["amount"],
    "date": data["date"]
    }
    subject, body = code_handler.handle_code(6, bill=bill)
    info = EmailMessage(receiver=email, subject=subject, body=body)
    email_service = EmailService()
    email_sent = email_service.send_email(info)
    if email_sent == 1:
        response = {
            'message':'done'
        }
        return jsonify(response), 200
    else:
        return jsonify({'message': 'couldnt send'}), 404
