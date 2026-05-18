from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from app.models import User, Note
from app.extensions import db
from app.utils.decorators import admin_required
from flask_login import logout_user, current_user

admin_bp = Blueprint('admin', __name__, template_folder='templates', static_folder='static')


@admin_bp.route('/dashboard')
@admin_required
def dashboard():
    title = "Admin dashboard"
    return render_template('admin/admin_dashboard.html', title=title)



@admin_bp.route('/users')
@admin_required
def users():
    title = "Users"
    users = User.query.all()
    return render_template('/admin/users.html', title=title, users=users)



@admin_bp.route('/notes')
@admin_required
def notes():
    title = "Notes"
    notes = Note.query.all()
    return render_template('admin/notes.html', notes = notes, title=title)



@admin_bp.route('/ban_user/<int:user_id>', methods=['POST'])
@admin_required
def ban_user(user_id):
    user=User.query.get(user_id)
    if not user:
        abort(403)

    if user.id == current_user.id:
        flash('You cannnot ban yourself')
        return redirect(url_for('admin.users'))
    try:
        user.is_banned = True

        db.session.commit()
        flash('The user was banned successfully')

    except Exception as e:

        return f"Error {e}"
    return redirect(url_for('admin.users'))



@admin_bp.route('/delete_user_note/<int:note_id>', methods=['POST'])
@admin_required
def delete_user_note(note_id):
    note=Note.query.get(note_id)
    if not note:
        abort(403)
    try:
        db.session.delete(note)
        db.session.commit()
        flash('The note was deleted successfully')

    except Exception as e:

        return f"Error {e}"
    return redirect(url_for('admin.notes'))


    