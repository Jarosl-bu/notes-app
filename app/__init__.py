from flask import Flask
from .extensions import db, login_manager
from app.notes.notes import notes_bp
from app.auth.auth import auth_bp
from app.admin.admin import admin_bp
import app.user_loader
from dotenv import load_dotenv
import os



load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///block.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    app.register_blueprint(notes_bp, url_prefix='/notes')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(admin_bp, url_prefix='/admin')

    db.init_app(app)

    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    
    with app.app_context():
        db.create_all() 

    return app