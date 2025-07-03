from sql_connection import get_sql_connection

if __name__ == "__main__":
    connection = get_sql_connection()
    if connection is not None:
        print("Database connection successful!")
        connection.close()
    else:
        print("Failed to connect to the database.")