# app/routes.py
from flask import Flask

from messages.adapters.In.controller import messageBP

app = Flask(__name__)
app.register_blueprint(messageBP)

app.run()