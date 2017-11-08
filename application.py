import os

from flask import Flask, request, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

class Name(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    message = db.Column(db.String(120), nullable=False)

    def __init__(self, name, message):
        self.name = name
        self.message = message

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sign', methods=["GET", "POST"])
def sign():
    if request.method == "POST":
        name = request.form.get('name')
        message = request.form.get('message')

        new_name = Name(name, message)

        try:
            db.session.add(new_name)
        except ValueError:
            return render_template('error.html')

        db.session.commit()

        return redirect(url_for('index'))

    else:
        return render_template('sign.html')
