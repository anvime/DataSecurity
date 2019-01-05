from flask_login import UserMixin
from flask_wtf import FlaskForm
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, BigInteger, String, ForeignKey, Unicode, Binary, LargeBinary, Time, DateTime, Date, Text, Boolean, Float, JSON
from sqlalchemy.orm import relationship, backref, deferred
from sqlalchemy.orm import sessionmaker
from src.app import db
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Length

class LoginForm(FlaskForm):
    login = StringField('login', validators=[InputRequired(), Length(min=4, max=15)])
    name = StringField('name', validators=[InputRequired(), Length(min=4, max=15)])
    lastname = StringField('lastname', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')

class RegisterForm(FlaskForm):
    login = StringField('login', validators=[InputRequired(), Length(min=4, max=15)])
    name = StringField('name', validators=[InputRequired(), Length(min=4, max=15)])
    lastname = StringField('lastname', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])

class User(UserMixin, db.Model):
	__tablename__ = "User"
	id = Column('id', Integer, primary_key=True, nullable=False)
	login = Column('login', Unicode, nullable=False)
	password = Column('password', Unicode, nullable=False)
	name = Column('Name', Unicode, nullable=False)
	lastname = Column('Lastname', Unicode, nullable=False)
	isDeleted = Column('isDeleted', Boolean, nullable=False)

