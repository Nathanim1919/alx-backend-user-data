#!/usr/bin/env python3
"""Main file"""
from flask import Flask, jsonify, make_response, redirect, request, abort
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


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login() -> str:
    """POST /sessions
    Return:
        - JSON payload of the form containing login info.
    """
    # Get user credentials from form data
    email, password = request.form.get("email"), request.form.get("password")
    # Check if the user's credentials are valid
    if not auth.valid_login(email, password):
        abort(401)
    # Create a new session for the user
    session_id = auth.create_session(email)
    # Construct a response with a JSON payload
    response = jsonify({"email": email, "message": "logged in"})
    # Set a cookie with the session ID on the response
    response.set_cookie("session_id", session_id)
    # Return the response
    return response


@app.route("/sessions", methods=["DELETE"], strict_slashes=False)
def logout() -> str:
    """Logout user
    """
    session_id = request.cookies.get("session_id")
    user = auth.get_user_from_session_id(session_id)
    if not user:
        abort(403)
    auth.destroy_session(user.id)
    return redirect("/")


@app.route("/profile", methods=["GET"], strict_slashes=False)
def profile() -> str:
    """GET /profile
    Return:
        - JSON payload of the form containing user profile info.
    """
    session_id = request.cookies.get("session_id")
    user = auth.get_user_from_session_id(session_id)
    if not user:
        abort(403)
    return jsonify({"email": user.email}), 200


@app.route('/get_reset_password_token', methods=['POST'], strict_slashes=False)
def get_reset_password_token():
    """Get Reset password token"""
    email = request.form.get("email")
    try:
        reset_token = auth.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": reset_token})
    except ValueError:
        abort(403)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
