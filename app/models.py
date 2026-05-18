from datetime import datetime 
from .extensions import db
from flask_login import UserMixin



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), nullable = False)
    email = db.Column(db.String(100), unique = True, nullable = False)
    password = db.Column(db.String(225), nullable = False)
    is_admin = db.Column(db.Boolean, default = False)
    is_banned = db.Column(db.Boolean, default = False)
    notes = db.relationship('Note', backref = 'author', lazy = True)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    type = db.Column(db.Text)
    title = db.Column(db.String(100), nullable = False)
    text = db.Column(db.Text, nullable = False)
    datetime = db.Column(db.DateTime, default = datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)