#!/usr/bin/env python3
"""Main file"""
from flask import Flask, jsonify, make_response, request, abort
from auth import Auth


app = Flask(__name__)
auth = Auth()


@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Bienvenue'})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users() -> str:
    """POST /users
    Return:
        - JSON payload of the form containing various information.
    """
    # Get the email and password from form data
    email, password = request.form.get("email"), request.form.get("password")
    try:
        # Register the user
        auth.register_user(email, password)
        # Respond with the following JSON payload:
        # {"email": "<registered email>", "message": "user created"}
        return jsonify({"email": email, "message": "user created"})
    # If the user is already registered, catch the exception and return a
    # JSON payload of the form: {"message": "email already registered"}
    # and return a 400 status code
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> str:
    email, password = request.form.get('email'), request.form.get('password')
    if (auth.valid_login(email, password)):
        session_id = auth.create_session(email)
        # store the session id as a cookie with key "session_id"
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie('session_id', session_id)
        # Respond with the following JSON payload:
        # {"email": "<registered email>", "message": "logged in"}
        return response
    else:
        abort(401)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
