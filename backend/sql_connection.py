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
        db_host = os.getenv("DB_HOST", "localhost")  # Default to localhost if not set
        db_user = os.getenv("DB_USER")
        db_password = os.getenv("DB_PASSWORD")
        db_name = os.getenv("DB_NAME")
        
        try:
            __cnx = mysql.connector.connect(
                host=db_host,
                user=db_user,
                password=db_password,
                database=db_name
            )
        except mysql.connector.Error as e:
            print(f"Error connecting to MySQL Database: {e}")
            __cnx = None

    return __cnx