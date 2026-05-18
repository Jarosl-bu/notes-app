from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from app.models import User
from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required

auth_bp = Blueprint('auth', __name__, template_folder='templates', static_folder='static')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():

    title = "Register"

    if request.method == "POST":
        try:
            
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']
            repeat_password = request.form['repeat_password']

            checked_email = User.query.filter_by(email=email).first()
            if checked_email:
                flash('This email has already been registered')
                return redirect(url_for('auth.login'))


            if password != repeat_password:
                flash('Your passwords are different.')
                return redirect(url_for('auth.register'))
            
            if len(password) < 8:
                flash ('Your password should contain 8 symbols.')
                return redirect(url_for('auth.register'))

            hashed_password = generate_password_hash(password)

            user = User(username = username, email = email, password = hashed_password)
            
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        except Exception as e:
            return f"Error{e}"
        
    return render_template('auth/register.html', title=title)

 

@auth_bp.route('/login', methods=['POST', 'GET'])
def login():

    title = "Log in"

    if request.method == 'POST':
        
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()

        if not user:
            flash('This account was not registered. Please register.')
            return redirect(url_for('auth.login'))
        
        if user.is_banned:
            abort(403)

        if check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('notes.index'))
        
        else:
            flash('Check your password or email')
            return redirect(url_for('auth.login'))
        
    return render_template('auth/login.html', title=title)
    

@auth_bp.route('/logout', methods=["POST"])
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
