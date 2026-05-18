from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from app.models import Note, User
from app.extensions import db
from flask_login import current_user, login_required


notes_bp = Blueprint('notes', __name__, template_folder='templates', static_folder='static')

@notes_bp.route('/')
@login_required
def index():
    notes = Note.query.filter_by(user_id = current_user.id).all()
    return render_template('notes/index.html', notes = notes)



@notes_bp.route('/create-note', methods = ["POST", "GET"])
@login_required
def create_note():
        
        if request.method  == "POST":

            try:

                note = Note(
                    type = request.form["note"],
                    title = request.form['title'],
                    text = request.form['text'],
                    author = current_user
                )
                db.session.add(note)
                db.session.commit()
                return redirect(url_for('.index'))
            
            except Exception as e:

                return f"Error{e}"
            
        return render_template('notes/create-note.html')



@notes_bp.route('/create-list', methods = ["POST", "GET"])
@login_required
def create_list():
        
        if request.method  == "POST":

            try:
                    type = request.form['list']
                    title = request.form['title']
                    texts = request.form.getlist('list_text[]')

                    full_text = "• " + "\n• ".join(texts)

                    note = Note(
                         type = type,
                         title = title,
                         text = full_text,
                         author = current_user
                    )

                    db.session.add(note)
                    db.session.commit()
                    return redirect(url_for('.index'))
            except Exception as e:

                return f"Error{e}"
            
        return render_template('notes/create-list.html')



@notes_bp.route('/delete/<int:note_id>', methods = ["POST"])
@login_required
def delete(note_id):

    note = Note.query.get(note_id)

    if note.user_id != current_user.id:
         abort(403)

    try:
        if note:
            db.session.delete(note)
            db.session.commit()
            flash('The note was deleted successfully')

    except Exception as e:

        return f"Error{e}"
        
    return redirect(url_for('.index'))



@notes_bp.route('/edit/<int:note_id>', methods = ["GET", "POST"])
@login_required
def edit(note_id):
    note = Note.query.get_or_404(note_id)

    if note.user_id != current_user.id:
        abort(403)

    if request.method == "POST":
        try:
            if note:
                if note.type == "text":
                     new_title = request.form["title"]
                     new_text = request.form.get("text")

                     if new_title and new_text:
                        note.title = new_title
                        note.text = new_text
                else:
                    new_title = request.form['title']
                    new_texts = request.form.getlist('list_text[]')
                    new_full_text = "• " + "\n• ".join(new_texts)

                    if new_title and new_full_text:
                         note.title = new_title
                         note.text = new_full_text

                db.session.commit()
                return redirect(url_for('.index'))

        except Exception as e:
            return f"Error{e}"
    else:
        if note:
            if note.type == "text":
                return render_template('notes/note-edit.html', note = note)
            else:
                return render_template('notes/list-edit.html', note = note)
