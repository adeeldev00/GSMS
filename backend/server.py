from flask import Flask, request, jsonify
from flask_cors import CORS
from sql_connection import get_sql_connection
import json
import os

import product_pao
import orders_pao
import uom_pao

app = Flask(__name__)
CORS(app, resources={
    r"/getUOM": {"origins": ["https://gsms-adeeldevs-projects-f7c6df64.vercel.app", "https://gsms-adeeldevs-projects-f7c6df64.vercel.app/", "http://localhost:8000"]},
    r"/getProducts": {"origins": ["https://gsms-adeeldevs-projects-f7c6df64.vercel.app", "https://gsms-adeeldevs-projects-f7c6df64.vercel.app/", "http://localhost:8000"]},
    r"/insertProduct": {"origins": ["https://gsms-adeeldevs-projects-f7c6df64.vercel.app", "https://gsms-adeeldevs-projects-f7c6df64.vercel.app/", "http://localhost:8000"]},
    r"/getAllOrders": {"origins": ["https://gsms-adeeldevs-projects-f7c6df64.vercel.app", "https://gsms-adeeldevs-projects-f7c6df64.vercel.app/", "http://localhost:8000"]},
    r"/insertOrder": {"origins": ["https://gsms-adeeldevs-projects-f7c6df64.vercel.app", "https://gsms-adeeldevs-projects-f7c6df64.vercel.app/", "http://localhost:8000"]},
    r"/deleteProduct": {"origins": ["https://gsms-adeeldevs-projects-f7c6df64.vercel.app", "https://gsms-adeeldevs-projects-f7c6df64.vercel.app/", "http://localhost:8000"]}
})

def get_db_connection():
    connection = get_sql_connection()
    if connection is None:
        raise Exception("Failed to connect to the database")
    return connection

@app.route('/getUOM', methods=['GET'])
def get_uom():
    try:
        connection = get_db_connection()
        response = uom_pao.get_uoms(connection)
        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if 'connection' in locals():
            connection.close()

@app.route('/getProducts', methods=['GET'])
def get_products():
    try:
        connection = get_db_connection()
        response = product_pao.get_all_products(connection)
        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if 'connection' in locals():
            connection.close()

@app.route('/insertProduct', methods=['POST'])
def insert_product():
    try:
        connection = get_db_connection()
        request_payload = json.loads(request.form['data'])
        product_id = product_pao.insert_new_product(connection, request_payload)
        return jsonify({'product_id': product_id})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if 'connection' in locals():
            connection.close()

@app.route('/getAllOrders', methods=['GET'])
def get_all_orders():
    try:
        connection = get_db_connection()
        response = orders_pao.get_all_orders(connection)
        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if 'connection' in locals():
            connection.close()

@app.route('/insertOrder', methods=['POST'])
def insert_order():
    try:
        connection = get_db_connection()
        request_payload = json.loads(request.form['data'])
        print("Received Payload:", request_payload)
        order_id = orders_pao.insert_order(connection, request_payload)
        return jsonify({'order_id': order_id})
    except Exception as e:
        print(f"Error in insert_order: {str(e)}")  # Log the error
        return jsonify({'error': str(e)}), 500
    finally:
        if 'connection' in locals():
            connection.close()

@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    try:
        connection = get_db_connection()
        return_id = product_pao.delete_product(connection, request.form['product_id'])
        return jsonify({'product_id': return_id})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if 'connection' in locals():
            connection.close()

if __name__ == "__main__":
    print("Starting Python Flask Server For Grocery Store Management System")
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port)