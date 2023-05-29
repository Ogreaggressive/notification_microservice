# app/routes.py
from flask import Flask

from adapters.In.controller import messageBP

app = Flask(__name__)
app.register_blueprint(messageBP)

app.run()