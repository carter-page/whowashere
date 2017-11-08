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

![git clone](/resources/git-clone.gif)

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
cd ~/Desktop/whowashere
virtualenv -p python3 venv
```

```bash
source venv/bin/activate
pip install -r requirements.txt
```

This code does not work as is, however, since is not connected to any database.

```python
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']`
```
We need to give the program a `DATABASE_URL` which we will get from Heroku PostgreSQL.


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

This has been provided for you in the `whowashere` repository, but you will have to do this on your own.

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

Our database name will be `user` corresponding to the name of the class and our column names will be `id` and `name` of types `Integer` and `String` respectively.

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
We switch out `db.execute` statements from the [CS50 Python Library](https://github.com/cs50/python-cs50/blob/develop/src/cs50/sql.py) for `db.session.add()` followed by `db.session.commit()`.
```python
db.execute("INSERT INTO user (name) VALUES (:name)", name=name)

new_user = User(name)
db.session.add(new_user)
db.session.commit()
```
We can implement a `SELECT` statement by using `query` following the class name.

```python
users = User.query.order_by(User.id).all()
```
Once we have switched to Flask-SQLAlchemy, all we need to do now is create our database.

# Create PostgreSQL Database
```bash
heroku addons:create heroku-postgresql:hobby-dev
heroku config
```
The `config` command will output the `DATABASE_URL` environment variable. For local testing, copy this `DATABASE_URL` and then type `touch .env`.

```bash
export FLASK_APP=application.py
export FLASK_DEBUG=1

export DATABASE_URL=[DATABASE_URL]
```

Now that we have generated a DATABASE_URL from Heroku, let's use a PostgreSQL GUI to take a look at our database.

# Postico
Download
https://eggerapps.at/postico/

Postico, with `DATABASE_URL` copied, click "New Favorite". The fields should be populated automatically. Click connect.

Time to create our table.

```
git push heroku master
```

Open up a python REPL in Heroku
```
heroku run python
from application import db
db.create_all()
exit()
```
Press refresh in the upper right hand corner

![postico refresh](/resources/postico-refresh.gif)

To run locally,
```
cd ~/Desktop/whowaswhere
source .env
flask run
```
To see our flask app on the web, run
```
heroku open
```
![update rows](/resources/update-rows.gif)
