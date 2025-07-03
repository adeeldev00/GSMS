from dotenv import load_dotenv
import os
import mysql.connector
import datetime

__cnx = None

def get_sql_connection():
    print("Opening mysql connection")
    global __cnx

    if __cnx is None:
        # Load environment variables from .env file
        load_dotenv()
        
        # Retrieve database credentials from environment variables
        db_host = os.getenv("DB_HOST")  # Remove default localhost; require it from .env
        db_user = os.getenv("DB_USER")
        db_password = os.getenv("DB_PASSWORD")
        db_name = os.getenv("DB_NAME")
        db_port = int(os.getenv("DB_PORT", 3306))  # Default to 3306 if not set
        ssl_ca = os.getenv("DB_SSL_CA")  # Path to ca.pem

        try:
            __cnx = mysql.connector.connect(
                host=db_host,
                port=db_port,
                user=db_user,
                password=db_password,
                database=db_name,
                ssl_ca=ssl_ca,  # Use the SSL certificate file
                ssl_disabled=False  # Enable SSL
            )
        except mysql.connector.Error as e:
            print(f"Error connecting to MySQL Database: {e}")
            __cnx = None

    return __cnx