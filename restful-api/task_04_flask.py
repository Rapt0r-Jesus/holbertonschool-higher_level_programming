#!/usr/bin/env python3
"""Simple RESTful API using Flask."""

from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}


@app.route("/", methods=["GET"])
def home():
    """ Endpoint """
    return "Welcome to the Flask API!"


@app.route("/data", methods=["GET"])
def get_usernames():
    """List of the usernames"""
    usernames = list(users.keys())
    return jsonify(usernames)


@app.route("/status", methods=["GET"])
def status():
    """Check the Endpoint status"""
    return "OK"


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """Return full user data by username."""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

    @app.route('/add_user', methods=["POST"])
def add_user():
    """Add a user."""
    data = request.get_json()

    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]
    users[username] = {
        "username": username,
        "name": data["name"],
        "age": data["age"],
        "city": data["city"]
    }
    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__":
    app.run(debug=True, port=5000)
app.run()
