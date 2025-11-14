#!/usr/bin/python3
"""
Flask application that renders a dynamic template
using loops and conditions from Jinja.
"""

from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/items')
def items():
    """Route that reads items from JSON and renders them."""

    try:
        with open("items.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            items = data.get("items", [])
    except Exception:
        items = []

    return render_template("items.html", items=items)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
