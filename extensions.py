from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

login_manager = LoginManager()
db = SQLAlchemy()
bcrypt = Bcrypt()

def hash_password(password):
    return bcrypt.generate_password_hash(password).decode('utf-8')

def check_password(password, hashed_password):
    return bcrypt.check_password_hash(hashed_password, password)