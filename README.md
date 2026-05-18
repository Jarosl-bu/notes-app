# Flask Notes App

A simple web application built with Flask for creating, managing, and organizing notes with user authentication and admin features.

---

## Features

- User registration and login
- Password hashing and authentication
- Create, edit, and delete notes
- Support for text and list-style notes
- Admin panel for user management
- Flash messages for notifications
- Bootstrap-based UI

---

## Tech Stack

- Python
- Flask
- Flask-Login
- Flask-SQLAlchemy
- SQLite
- Bootstrap 5
- HTML / CSS / Jinja2

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Jarosl-bu/flask-notes-app.git
cd flask-notes-app

### 2. Create virtual environment

```bash
python -m venv venv
```

### 3. Activate environment

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate
### 4. Install dependencies
pip install -r requirements.txt
⚙️ Environment Variables

Create a .env file in the root directory:

SECRET_KEY=your_secret_key_here
FLASK_ENV=development
▶️ Run the app
python run.py

Then open:

http://127.0.0.1:5000/
📁 Project Structure
project/
│
├── app/
│   ├── auth/
│   ├── notes/
│   ├── admin/
│   ├── templates/
│   ├── static/
│   └── models.py
│
├── instance/
├── .env
├── .gitignore
├── requirements.txt
├── run.py
🔐 Security
Passwords are hashed using Werkzeug
Admin routes are protected
User authentication via Flask-Login
Secret key stored in environment variables
🚀 Future Improvements
Search functionality
Pagination
REST API
Docker support
PostgreSQL integration
