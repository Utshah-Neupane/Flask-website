from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = 'a921454d727093c2b06b82c7'
db = SQLAlchemy(app)


from market.models import Item, User
from market import routes
