#!/usr/bin/env python3
from flask import Flask, request, abort, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base, User, Booking
from util import Validator, ApiResponseHandler
from datetime import datetime


def create_app(db_uri):
    app = Flask(__name__)
    engine = create_engine(db_uri)
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    # Constants
    ERROR_CONTEXT = 'error'
    SUCCESS_CONTEXT = 'success'
    INFO_CONTEXT = 'info'
    HTTP_BAD_REQUEST = 400
    HTTP_NOT_FOUND = 404
    HTTP_METHOD_NOT_ALLOWED = 405

    # This gives a simple description for the API
    @app.route('/')
    def index():
        return ApiResponseHandler.prepare(
            INFO_CONTEXT,
            'Simple flight booking service. Please refer to API documentation',
            201
        )

    # This commits a booking for a given user
    @app.route('/commit', methods=['POST'])
    def commit():
        payload = request.json
        err_msg = Validator.commit(payload)
        if err_msg is not None:
            abort(400, err_msg)

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
        return ApiResponseHandler.prepare(SUCCESS_CONTEXT, str(booking.id), 201)

    # This returns the list of booked flights of a given user
    @app.route('/bookings/<int:user_id>', methods=['GET'])
    def bookings(user_id):
        bookings = session.query(Booking).filter_by(user_id=user_id).all()
        return jsonify([i.serialize for i in bookings]), 200

    # This handles 400 BAD REQUEST errors
    @app.errorhandler(HTTP_BAD_REQUEST)
    def bad_request(e):
        return ApiResponseHandler.prepare(ERROR_CONTEXT, e.description, HTTP_BAD_REQUEST)

    # This handles 404 NOT FOUND errors
    @app.errorhandler(HTTP_NOT_FOUND)
    def not_found(e):
        return ApiResponseHandler.prepare(ERROR_CONTEXT, e.description, HTTP_NOT_FOUND)

    # This handles 405 METHOD NOT ALLOWED errors
    @app.errorhandler(HTTP_METHOD_NOT_ALLOWED)
    def method_not_allowed(e):
        return ApiResponseHandler.prepare(ERROR_CONTEXT, e.description, HTTP_METHOD_NOT_ALLOWED)

    return app


if __name__ == '__main__':
    app = create_app('sqlite:///direct-booking.db')
    app.run(host='0.0.0.0')
