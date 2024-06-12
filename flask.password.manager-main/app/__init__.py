from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from cryptography.fernet import Fernet
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

try:
    cipher_suite = Fernet(app.config['SECRET_KEY'])
except ValueError as e:
    raise ValueError("Invalid SECRET_KEY. Ensure it is a valid base64-encoded 32-byte key.") from e

from app import routes
