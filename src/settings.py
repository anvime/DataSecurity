from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src import dbSetup
# dbSetup.setup()

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_ECHO'] = False
app.config['SECRET_KEY'] = 'xcjytebjby6 yycefgjydtvh b'
db = SQLAlchemy(app)
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
REMEMBER_COOKIE_HTTPONLY = True