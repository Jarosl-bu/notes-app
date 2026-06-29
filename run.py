from app import create_app
from app.models import User
from app import db
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    if not User.query.filter_by(email="admin@gmail.com").first():
        admin = User(
            username="Admin",
            email="admin@gmail.com",
            password=generate_password_hash("12345678"),
            is_admin=True,
        )
        db.session.add(admin)
        db.session.commit()

if __name__ == "__main__":
    app.run(debug=True)