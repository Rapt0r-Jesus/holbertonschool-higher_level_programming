#!/usr/bin/python3
"""
Flask app that loads product data from JSON, CSV, or SQLite
and displays it using a single dynamic template.
"""

from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def read_json_file():
    """Read products from JSON file."""
    try:
        with open("products.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None


def read_csv_file():
    """Read products from CSV file."""
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


def read_sqlite_data():
    """Read products from SQLite database."""
    try:
        conn = sqlite3.connect("products.db")
        cursor = conn.cursor()

        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()

        conn.close()

        # Convert SQL rows to list of dicts
        return [
            {"id": row[0], "name": row[1], "category": row[2], "price": row[3]}
            for row in rows
        ]
    except Exception:
        return None


@app.route("/products")
def products():
    """Display products depending on the source (json, csv, sql)."""
    source = request.args.get("source")
    product_id = request.args.get("id")

    # Validate source
    if source not in ("json", "csv", "sql"):
        return render_template("product_display.html",
                               error="Wrong source",
                               products=[])

    # Determine data source
    if source == "json":
        data = read_json_file()
    elif source == "csv":
        data = read_csv_file()
    else:  # source == "sql"
        data = read_sqlite_data()

    if data is None:
        return render_template("product_display.html",
                               error="Error loading data",
                               products=[])

    # Optional filtering by ID
    if product_id:
        try:
            product_id = int(product_id)
            filtered = [p for p in data if p["id"] == product_id]

            if not filtered:
                return render_template("product_display.html",
                                       error="Product not found",
                                       products=[])
            data = filtered
        except ValueError:
            return render_template("product_display.html",
                                   error="Invalid ID format",
                                   products=[])

    return render_template("product_display.html",
                           products=data,
                           error=None)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
