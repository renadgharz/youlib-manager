from sqlalchemy import Column, Integer, String, DateTime
from flask_login import UserMixin
from datetime import datetime

from extensions import db, login_manager, hash_password, check_password


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, index=True, nullable=False)
    email = db.Column(db.String(100), unique=True, index=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    joined_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = hash_password(password)

    def check_password(self, password):
        return check_password(password, self.check_password)

    def __repr__(self):
        return f"User('{self.username})', '{self.email}', '{self.joined_at}'"

@login_manager.user_loader
def load_user():
    return User.get_id()