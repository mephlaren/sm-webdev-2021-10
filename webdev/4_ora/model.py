from sqla_wrapper import SQLAlchemy
from sqlalchemy import ForeignKey

db = SQLAlchemy("sqlite:///gtsn.sqlite")

class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=False)
    guess = db.Column(db.Integer, unique=False)

class Secret(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, unique=False)
    user_id =db.Column(db.Integer, ForeignKey("User.id"))