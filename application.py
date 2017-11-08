import os

from flask import Flask, request, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name

@app.route('/')
def index():
    users = User.query.order_by(User.id).all()
    return render_template('index.html', users=users)

@app.route('/sign', methods=["GET", "POST"])
def sign():
    if request.method == "POST":
        name = request.form.get('name')

        if name == "" or name.isspace():
            return "Name cannot be empty!"

        new_user = User(name)

        if User.query.filter(User.name == name).first() != None:
             return name + " has already been here!"

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('index'))

    else:
        return render_template('sign.html')
