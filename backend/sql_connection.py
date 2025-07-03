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
        db_user = os.getenv("DB_USER")
        db_password = os.getenv("DB_PASSWORD")
        db_name = os.getenv("DB_NAME")
        
        # Connect to the database
        __cnx = mysql.connector.connect(
            user=db_user,
            password=db_password,
            database=db_name
        )

    return __cnx