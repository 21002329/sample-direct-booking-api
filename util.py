from flask import jsonify, make_response


class Validator():
    def commit(booking):
        mandatory = ['user_id',
                     'book_date',
                     'amount',
                     'merchant_id',
                     'flight_date',
                     'flight_origin',
                     'flight_dest',
                     'flight_nr']

        if not all(key in booking for key in mandatory):
            return 'Missing one or more mandatory parameters for commit service'

        return None


class ErrorHandler():
    def prepare(desc, status):
        return make_response(jsonify({'error': desc}), status)
