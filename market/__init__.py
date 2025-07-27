from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = 'a921454d727093c2b06b82c7'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


from market.models import Item, User
from market import routes
