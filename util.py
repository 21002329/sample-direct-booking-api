from flask import jsonify, make_response


class Validator():
    def commit(booking):
        mandatory = ['user_id',
                     'amount',
                     'merchant_id',
                     'ext_ref_nr']

        if not all(key in booking for key in mandatory):
            return 'Missing one or more mandatory parameters'

        return None


class ErrorHandler():
    def prepare(desc, status):
        return make_response(jsonify({'error': desc}), status)
