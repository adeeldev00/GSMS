from sql_connection import get_sql_connection

def get_all_products(connection):
    cursor = connection.cursor()
    query = ("select products.product_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name from products inner join uom on products.uom_id=uom.uom_id")
    cursor.execute(query)
    response = []
    for (product_id, name, uom_id, price_per_unit, uom_name) in cursor:
        response.append({
            'product_id': product_id,
            'name': name,
            'uom_id': uom_id,
            'price_per_unit': price_per_unit,
            'uom_name': uom_name
        })
    return response

def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("INSERT INTO products "
             "(name, uom_id, price_per_unit)"
             "VALUES (%s, %s, %s)")
    data = (product['product_name'], product['uom_id'], product['price_per_unit'])

    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products where product_id=" + str(product_id))
    cursor.execute(query)
    connection.commit()

    return cursor.lastrowid

if __name__ == '__main__':
    connection = get_sql_connection()
    # print(get_all_products(connection))
    print(insert_new_product(connection, {
        'product_name': 'potatoes',
        'uom_id': '1',
        'price_per_unit': 10
    }))

    
# import mysql.connector

# def get_all_products():
# # Connect to MySQL
#   cnx = mysql.connector.connect(
#     user='root',
#     password='358797324705@Adeel',
#     host='127.0.0.1',
#     database='python_grocerymanagementsystem_db'  # use correct lowercase DB name
# )

#   cursor = cnx.cursor()

# # Correct query as one string
#   query = """
# SELECT 
#     products.product_id, 
#     products.name, 
#     products.uom_id, 
#     products.price_per_unit, 
#     uom.uom_name
# FROM 
#     products
# INNER JOIN 
#     uom ON products.uom_id = uom.uom_id;
# """

#   cursor.execute(query)

#   response = []
# # Print results
#   for (product_id, name, uom_id, price_per_unit, uom_name) in cursor:
#     print(f"Product ID: {product_id}, Name: {name}, UOM ID: {uom_id}, Price per Unit: {price_per_unit}, UOM Name: {uom_name}")
#     response.append({
#         'product_id': product_id,
#         'name': name,
#         'uom_id': uom_id,
#         'price_per_unit': price_per_unit,
#         'uom_name': uom_name
#     })

# # Close connection
#   cnx.close()

#   return response

# if __name__ == '__main__':
#     print(get_all_products())