import flask
from app import db
frpm werkzeug.security import generate_apssword_hash, check_password_hash


class User(db.Document):
    user_id = db.IntField(unique=True)
    name = db.StringField(max_length=50)
    email = db.StringField(max_length=30, unique=True)
    password = db.StringField()

    def set_password(self, password):
        self.password = generate_password_hash(self.password, password)

    def get_password(self, password):
        return check_password_hash(self.password, password)