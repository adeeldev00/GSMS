from dotenv import load_dotenv
import os
import mysql.connector
import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

__cnx = None

# def get_sql_connection():
#     print("Opening mysql connection")
#     global __cnx

#     if __cnx is None:
#         # Load environment variables from .env file
#         load_dotenv()
        
#         # Retrieve database credentials from environment variables
#         db_host = os.getenv("DB_HOST")
#         db_user = os.getenv("DB_USER")
#         db_password = os.getenv("DB_PASSWORD")
#         db_name = os.getenv("DB_NAME")
#         db_port = int(os.getenv("DB_PORT", 24599))  # Default to 24599 for Aiven
#         ssl_ca = os.getenv("DB_SSL_CA")  # Path to ca.pem

#         try:
#             __cnx = mysql.connector.connect(
#                 host=db_host,
#                 port=db_port,
#                 user=db_user,
#                 password=db_password,
#                 database=db_name,
#                 ssl_ca=ssl_ca,  # Use the SSL certificate file
#                 ssl_disabled=False  # Enable SSL
#             )
#         except mysql.connector.Error as e:
#             logger.error(f"Database connection failed: {e}")
#             __cnx = None

#     return __cnx
def get_sql_connection():
    print("Opening mysql connection")
    load_dotenv()
    db_host = os.getenv("DB_HOST")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_name = os.getenv("DB_NAME")
    db_port = int(os.getenv("DB_PORT", 3306))
    ssl_ca = os.getenv("DB_SSL_CA")

    try:
        connection = mysql.connector.connect(
            host=db_host,
            port=db_port,
            user=db_user,
            password=db_password,
            database=db_name,
            ssl_ca=None if not ssl_ca else ssl_ca,
            ssl_disabled=True if not ssl_ca else False
        )
        return connection
    except mysql.connector.Error as e:
        logger.error(f"Database connection failed: {e}")
        return None

# from dotenv import load_dotenv
# import os
# import mysql.connector

# def get_sql_connection():
#     print("Opening mysql connection")
#     # Load .env.local for local testing, fall back to .env
#     load_dotenv(".env.local", override=True)  # Override with local settings if present
#     db_host = os.getenv("DB_HOST")
#     db_port = int(os.getenv("DB_PORT", 3306))  # Default to 3306 for local
#     db_user = os.getenv("DB_USER")
#     db_password = os.getenv("DB_PASSWORD", "")  # Default to empty if not set
#     db_name = os.getenv("DB_NAME")
#     ssl_ca = os.getenv("DB_SSL_CA")

#     try:
#         connection = mysql.connector.connect(
#             host=db_host,
#             port=db_port,
#             user=db_user,
#             password=db_password,
#             database=db_name,
#             ssl_ca=ssl_ca if ssl_ca else None,
#             ssl_disabled=ssl_ca is None
#         )
#         return connection
#     except mysql.connector.Error as e:
#         print(f"Error connecting to MySQL Database: {e}")
#         return None