import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, BigInteger, String, ForeignKey, Unicode, Binary, LargeBinary, Time, DateTime, Date, Text, Boolean, Float, JSON
from sqlalchemy.orm import relationship, backref, deferred, scoped_session
from sqlalchemy.orm import sessionmaker

def setup():
    engine = create_engine('sqlite:///db.db?check_same_thread=False')

    Base = declarative_base()

    class User(Base):
        __tablename__ = "User"
        id = Column('id', Integer, primary_key=True, nullable=False)
        login = Column('login', Unicode, nullable=False)
        password = Column('password', Unicode, nullable=False)
        name = Column('Name', Unicode, nullable=False)
        lastname = Column('Lastname', Unicode, nullable=False)
        isDeleted = Column('isDeleted', Boolean, nullable=False)

        def __repr__(self):
            return f"User('{self.id}','{self.login}','{self.password}','{self.name}','{self.lastname}','{self.isDeleted}') "


    Base.metadata.create_all(engine)
    # Example creation of record
    Session = sessionmaker(bind=engine)
    session = scoped_session(sessionmaker(bind=engine))
    # prod1 = Product(name = 'Apaszka Londyn',currentPrice = '120 zł', originalPrice='120 zł')
    # session.add(prod1)
    # prod2 = Product(name = 'Apaszka Paryż',currentPrice = '120 zł', originalPrice='120 zł')
    # session.add(prod2)
    # prod3 = Product(name = 'Apaszka Tokyo',currentPrice = '120 zł', originalPrice='120 zł')
    # session.add(prod3)
    # session.commit()
    #Adding new record
    #session.commit()