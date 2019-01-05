from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from src import dbSetup

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'xcjytebjby6 yycefgjydtvh b'
db = SQLAlchemy(app)
dbSetup.setup()
from src import dbModel

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(port=5000)