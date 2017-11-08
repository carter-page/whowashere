# CS50 Seminar - Publishing Your Flask App to the Web



# CS50 IDE
cd into project directory
```bash
cd ~/whowashere
git init
git add .
git commit -m "first commit"
```

![git init](/resources/cs50ide-git-init.gif)

# GitHub
New repository, which you name as your project.

![create repo](/resources/github-create-repo.gif)

Get Student Developer Pack for unlimited private repos
https://education.github.com/pack

# CS50 IDE
```bash
git remote add origin [URL]
git push -u origin master
```
![remote add](/resources/remote-add.png)

# Your Mac

Go to finder and open Terminal

![terminal](/resources/terminal.gif)

Homebrew
```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

![homebrew](/resources/homebrew.gif)

```bash
brew install git
cd ~/Desktop
git clone [URL]
```

```bash
brew install python
brew install python3
```

```bash
brew install virtualenv
```

Download Atom
https://atom.io


```bash
virtualenv -p python3 venv
```

```bash
source venv/bin/activate
pip install -r requirements.txt
```

# Heroku

```
brew install heroku/brew/heroku
```

Create heroku account
https://signup.heroku.com

```bash
heroku login
cd ~/whowashere
heroku create
```

# Procfile

```bash
pip install gunicorn
touch Procfile
web: gunicorn application:app
```

```bash
pip freeze > requirements.txt
```

# Switch out our SQLite for PostgreSQL
**Most difficult part**

```
pip install Flask-SQLAlchemy
```

Removed
```python
from cs50 import SQL
...
db = SQL("sqlite:///finance.db")
```

```python
import os
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
```

```python
db.execute("INSERT INTO user (name) VALUES (:name)", name=name)

new_user = User(name)
db.session.add(new_user)
db.session.commit()
```

```python
users = User.query.order_by(User.id).all()
```

# Create PostgreSQL Database
```bash
heroku addons:create heroku-postgresql:hobby-dev
heroku config
```

```bash
touch .env

export FLASK_APP=application.py
export FLASK_DEBUG=1

export DATABASE_URL=[DATABASE_URL]
```

# Postico
https://eggerapps.at/postico/

Postico, with url copied, click "New Favorite"


```
git push heroku master
```

```
heroku run python
from application import db
db.create_all()
exit()
```

```
flask run
```
```
heroku open
```
