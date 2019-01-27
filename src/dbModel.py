from src.settings import db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship, backref, deferred
from sqlalchemy.orm import sessionmaker


class Users (db.Model):
    __tablename__ = "User"
    id = db.Column('id', db.Integer, primary_key=True)
    username = db.Column('username', db.String(20), unique=True, nullable=False)
    email = db.Column('email', db.String(120), unique=True, nullable=False)
    password = db.Column('password', db.String(250), unique=True, nullable=False)
    question = db.Column('question', db.String(250), nullable=False)
    answer = db.Column('answer', db.String(250), nullable=False)

class Posts (db.Model):
    __tablename__ = "Post"
    id = db.Column('id', db.Integer, primary_key=True)
    post = db.Column('post', db.String(250), nullable=False)
    userID = db.Column('userID', db.Integer, nullable=False)
