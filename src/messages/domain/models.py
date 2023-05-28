class EmailMessage:
    def __init__(self, receiverId=None, receiver=None, subject=None, body=None):
        self.receiverId = receiverId
        self.receiver = receiver
        self.subject = subject
        self.body = body