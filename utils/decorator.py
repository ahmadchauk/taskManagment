from functools import wraps
from flask import jsonify, request, make_response
from werkzeug.exceptions import BadRequest


def handle_api_errors(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if request.method == "GET" or request.method == "DELETE":
            return f(*args, **kwargs)
        try:
            data = request.get_json()
            if data is None:
                return make_response(jsonify({"error": "Bad request exception"}), 500)
        except BadRequest:
            return make_response(jsonify({"error": "Bad request exception"}), 500)

        return f(*args, **kwargs)

    return wrapper
