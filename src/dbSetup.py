import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, BigInteger, String, ForeignKey, Unicode, Binary, LargeBinary, Time, DateTime, Date, Text, Boolean, Float, JSON
from sqlalchemy.orm import relationship, backref, deferred, scoped_session
from sqlalchemy.orm import sessionmaker

def setup():
    engine = create_engine('sqlite:///db.db?check_same_thread=False')

    Base = declarative_base()

    class Users(Base):
        __tablename__ = "User"
        id = Column('id', Integer, primary_key=True)
        username = Column('username', String(20), unique=True, nullable=False)
        email = Column('email', String(120), unique=True, nullable=False)
        password = Column('password', String(250), unique=True, nullable=False)

        def __repr__(self):
            return f"User('{self.id}','{self.username}','{self.email}') "

    class Posts(Base):
        __tablename__ = "Post"
        id = Column('id', Integer, primary_key=True)
        post = Column('post', String(250),  nullable=False)
        userID = Column('userID', Integer, nullable=False)

        def __repr__(self):
            return f"User('{self.id}','{self.post}','{self.userID}')"

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = scoped_session(sessionmaker(bind=engine))
    setup()
