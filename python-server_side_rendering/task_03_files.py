#!/usr/bin/python3
"""
Flask app that loads product data from JSON or CSV
and displays it using a dynamic template.
"""

from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


def read_json_file():
    """Read products from JSON file."""
    try:
        with open("products.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None


def read_csv_file():
    """Read products from CSV file and convert rows to dictionaries."""
    try:
        products = []
        with open("products.csv", "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                })
        return products
    except Exception:
        return None


@app.route("/products")
def products():
    """Display products depending on query parameters."""
    source = request.args.get("source")
    product_id = request.args.get("id")

    # Validate source
    if source not in ("json", "csv"):
        return render_template("product_display.html", error="Wrong source", products=[])

    # Load data based on source
    if source == "json":
        data = read_json_file()
    else:
        data = read_csv_file()

    if data is None:
        return render_template("product_display.html", error="Error reading file", products=[])

    # Filter data by id if provided
    if product_id:
        try:
            product_id = int(product_id)
            data = [p for p in data if p.get("id") == product_id]

            if not data:
                return render_template("product_display.html", error="Product not found", products=[])
        except ValueError:
            return render_template("product_display.html", error="Invalid ID format", products=[])

    # Render template with products
    return render_template("product_display.html", products=data, error=None)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
