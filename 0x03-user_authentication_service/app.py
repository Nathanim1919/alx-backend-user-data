#!/usr/bin/env python3
"""Main file"""
from flask import Flask, jsonify, request
from auth import Auth


app = Flask(__name__)
auth = Auth()


@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Bienvenue'})


@app.route('/users', methods=['POST'])
def users():
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        auth.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

    return jsonify({"email":email,"message": "user created"}), 201


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
