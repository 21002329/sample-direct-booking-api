#!/usr/bin/env python3
from flask import Flask, request, abort, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base, User, Booking
from util import Validator, ErrorHandler
from datetime import datetime

app = Flask(__name__)

# Persistence
engine = create_engine('sqlite:///direct_booking.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Constants
HTTP_BAD_REQUEST = 400
HTTP_NOT_FOUND = 404
HTTP_METHOD_NOT_ALLOWED = 405


# This gives a simple description for the API
@app.route('/')
def index():
    return jsonify({'info': 'Simple flight booking service. Please refer to API documentation'}), 201


# This commits a booking for a given user
@app.route('/commit', methods=['POST'])
def commit():
    payload = request.json
    err = Validator.commit(payload)
    if err is not None:
        abort(400, err)

    book_date = datetime.strptime(payload['book_date'], '%Y%m%d%H%M')
    flight_date = datetime.strptime(payload['flight_date'], '%Y%m%d%H%M')
    booking = Booking(user_id=payload['user_id'],
                      book_date=book_date,
                      amount=payload['amount'],
                      merchant_id=payload['merchant_id'],
                      flight_date=flight_date,
                      flight_origin=payload['flight_origin'],
                      flight_dest=payload['flight_dest'],
                      flight_nr=payload['flight_nr'])

    session.add(booking)
    session.commit()
    return jsonify({'info': 'Commited booking'}), 201


# This returns the list of booked flights of a given user
@app.route('/bookings/<int:user_id>', methods=['GET'])
def bookings(user_id):
    bookings = session.query(Booking).filter_by(user_id=user_id).all()
    return jsonify(Bookings=[i.serialize for i in bookings]), 201


# This handles 400 BAD REQUEST errors
@app.errorhandler(HTTP_BAD_REQUEST)
def bad_request(e):
    return ErrorHandler.prepare(e.description, HTTP_BAD_REQUEST)


# This handles 404 NOT FOUND errors
@app.errorhandler(HTTP_NOT_FOUND)
def not_found(e):
    return ErrorHandler.prepare(e.description, HTTP_NOT_FOUND)


# This handles 405 METHOD NOT ALLOWED errors
@app.errorhandler(HTTP_METHOD_NOT_ALLOWED)
def method_not_allowed(e):
    return ErrorHandler.prepare(e.description, HTTP_METHOD_NOT_ALLOWED)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
