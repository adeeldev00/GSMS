from flask import Flask, request, jsonify
from flask_cors import CORS
from sql_connection import get_sql_connection
import json
import os

import product_pao
import orders_pao
import uom_pao

app = Flask(__name__)
CORS(app)

# Remove global connection variable; handle it per request
def get_db_connection():
    connection = get_sql_connection()
    if connection is None:
        raise Exception("Failed to connect to the database")
    return connection

@app.route('/getUOM', methods=['GET'])
def get_uom():
    connection = get_db_connection()
    try:
        response = uom_pao.get_uoms(connection)
        return jsonify(response)
    finally:
        connection.close()

@app.route('/getProducts', methods=['GET'])
def get_products():
    connection = get_db_connection()
    try:
        response = product_pao.get_all_products(connection)
        return jsonify(response)
    finally:
        connection.close()

@app.route('/insertProduct', methods=['POST'])
def insert_product():
    connection = get_db_connection()
    try:
        request_payload = json.loads(request.form['data'])
        product_id = product_pao.insert_new_product(connection, request_payload)
        return jsonify({'product_id': product_id})
    finally:
        connection.close()

@app.route('/getAllOrders', methods=['GET'])
def get_all_orders():
    connection = get_db_connection()
    try:
        response = orders_pao.get_all_orders(connection)
        return jsonify(response)
    finally:
        connection.close()

@app.route('/insertOrder', methods=['POST'])
def insert_order():
    connection = get_db_connection()
    try:
        request_payload = json.loads(request.form['data'])
        order_id = orders_pao.insert_order(connection, request_payload)
        return jsonify({'order_id': order_id})
    finally:
        connection.close()

@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    connection = get_db_connection()
    try:
        return_id = product_pao.delete_product(connection, request.form['product_id'])
        return jsonify({'product_id': return_id})
    finally:
        connection.close()

if __name__ == "__main__":
    print("Starting Python Flask Server For Grocery Store Management System")
    port = int(os.getenv("PORT", 5000))  # Use Render's PORT or default to 5000
    app.run(host='0.0.0.0', port=port)