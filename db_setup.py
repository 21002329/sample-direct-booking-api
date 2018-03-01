import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    name = Column(String(250))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'email': self.email,
            'name': self.name
        }


class Booking(Base):
    __tablename__ = 'booking'

    id = Column(Integer, primary_key=True)
    book_date = Column(DateTime, nullable=False)
    amount = Column(Float, nullable=False)
    merchant_id = Column(Integer, nullable=False)
    flight_date = Column(DateTime, nullable=False)
    flight_origin = Column(String(250), nullable=False)
    flight_dest = Column(String(250), nullable=False)
    flight_nr = Column(Integer)
    
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'book_date': self.book_date,
            'amount': self.amount,
            'merchant_id': self.merchant_id,
            'flight_date': self.flight_date,
            'flight_origin': self.flight_origin,
            'flight_dest': self.flight_dest,
            'flight_nr': self.flight_nr,
        }


engine = create_engine('sqlite:///direct_booking.db')


Base.metadata.create_all(engine)
