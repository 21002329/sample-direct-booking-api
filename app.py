#!/usr/bin/env python3
from flask import Flask, request, abort
from util import Validator, ErrorHandler

app = Flask(__name__)


# Services
@app.route('/')
def index():
    return "Hello, World!"


# This commits a booking for a given user
@app.route('/commit', methods=['POST'])
def commit():
    err = Validator.commit(request.json)
    if err is not None:
        abort(400, err)

    return jsonify({'hi': 'commit'}), 201


# This returns the list of booked flights of a given user
@app.route('/bookings/<int:user_id>', methods=['GET'])
def bookings(user_id):

    return jsonify({'hello': 'bookings'}), 201


# This handles 400 BAD REQUEST errors
@app.errorhandler(400)
def bad_request(error):
    return ErrorHandler.prepare(error.description, 400)


# This handles 404 NOT FOUND errors
@app.errorhandler(404)
def not_found(error):
    return ErrorHandler.prepare(error.description, 404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
