import binascii
import cgi
import datetime
import hashlib
import json
import os
import random
import re
import time
import requests
from flask import Flask, render_template, redirect, session, request
from flask_recaptcha import ReCaptcha
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash
from src import dbModel
from src.settings import app, db

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index')
def indexx():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/signUp', methods=['POST'])
def signUp():
    _username = request.form['login']
    _email = request.form['email']
    _password = request.form['password']

    if not validateUsername(_username):
        return render_template("notify.html",
                               messageContent="Nazwa użytkownika może zawierać litery, cyfry, znak '.' oraz '_', pozostałe znaki są niedozwolone!")

    if not validateEmail(_email):
        return render_template('notify.html', messageContent="Niepoprawny email")

    _hashedPassword = hashPassword(_password)

    usernameAlreadyExists = dbModel.Users.query.filter_by(username=_username).first()
    if usernameAlreadyExists:
        return render_template('notify.html', messageContent="Nazwa użytkownika zajęta")

    emialAlreadyExists = dbModel.Users.query.filter_by(email=_email).first()
    if emialAlreadyExists:
        return render_template('notify.html', messageContent="Adres email zajęty")

    new_user = dbModel.Users(username=_username, email=_email, password=_hashedPassword)
    db.session.add(new_user)
    db.session.commit()

    # admin
    # Enter12345!

    return render_template('notify.html',
                           messageContent="Użytkownik zarejestrowany pomyślnie")

@app.route('/signIn', methods=['POST'])
def signIn():
    _username = request.form['login']
    _password = request.form['password']

    if not validateUsername(_username):
        return render_template("notify.html", messageContent="Błedny login lub hasło")

    user_to_signin = dbModel.Users.query.filter_by(username=_username).first()

    if user_to_signin:
        if verifyPassword(user_to_signin.password, _password):
            session['user'] = _username
            return redirect('/userHome')
    return render_template('notify.html', messageContent="Błędny login lub hasło")


@app.route('/userHome', methods=['GET'])
def userHome():
    if session.get('user'):
        username = cgi.escape(session['user'])
        userID = dbModel.Users.query.filter_by(username=username).first()
        userID = userID.id
        postslist = dbModel.Posts.query.filter_by(userID=userID).order_by(dbModel.Posts.id.desc()).all()
        return render_template('home.html', username=username, postslist=postslist)
    else:
        return redirect('/')

@app.route('/post', methods=['POST'])
def post():
    if request.method == 'POST':
        if session.get('user'):
            _post = request.form['post']
            if validatePost(_post):

                username = (session['user'])
                userID=dbModel.Users.query.filter_by(username=username).first()
                userID=userID.id

                newPost = dbModel.Posts(post=_post, userID=userID)
                db.session.add(newPost)
                db.session.commit()

                postslist=dbModel.Posts.query.filter_by(userID=userID).order_by(dbModel.Posts.id.desc()).all()

                return render_template('home.html', username=username, postslist=postslist)
            return render_template('notify.html', messageContent="Niepoprawny post")
    return 0


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')


def verifyPassword(dbPassword, formPassword):
    salt = dbPassword[:64]
    storedPassword = dbPassword[64:]
    passwdhash = hashlib.pbkdf2_hmac('sha512',
                                     formPassword.encode('utf-8'),
                                     salt.encode('ascii'),
                                     100000)
    passwdhash = binascii.hexlify(passwdhash).decode('ascii')
    return passwdhash == storedPassword


def hashPassword(password):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    passwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                     salt, 100000)
    passwdhash = binascii.hexlify(passwdhash)
    return (salt + passwdhash).decode('ascii')


def validateEmail(email):
    return re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email)


def validateUsername(username):
    return re.match(r"^[a-zA-Z0-9]+([._]?[a-zA-Z0-9]+)*$", username)

def validatePost(post):
    if len(post) > 250:
        return False
    blacklist = ['<', '>', '{', '}', '/', '\\', '*', '_', 'kurwa', 'yolo']

    if any([x in post for x in blacklist]):
        return False
    return re.match(r"", post)

@app.route('/changePasswd')
def changePasswd():
    return render_template('changePassword.html')

@app.route('/changePassword', methods=['POST'])
def changePassword():
    _oldPassword = request.form['oldPassword']
    _newPassword = request.form['password']
    _username = session['user']

    user = dbModel.Users.query.filter_by(username=_username).first()

    if verifyPassword(user.password, _oldPassword):
        _hashedNewPassword = hashPassword(_newPassword)

        delayAction()

        user.password = _hashedNewPassword
        db.session.commit()

        return render_template('notify.html', messageContent="Hasło zostało zmienione")

    else:
        return render_template('notify.html',
                               messageContent="Błędne hasło")

@app.route('/delete', methods=['POST'])
def deletepost():
    postID=request.form['postID']
    post = dbModel.Posts.query.filter_by(id=postID).first()
    db.session.delete(post)
    db.session.commit()
    return redirect('/userHome')

def delayAction():
    delayTime = random.uniform(0,1)
    time.sleep(delayTime)

if __name__ == '__main__':
    app.run(port=5000, ssl_context=('cert.pem', 'key.pem'))
