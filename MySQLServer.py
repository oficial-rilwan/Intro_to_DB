import mysql.connector
from mysql.connector import errorcode

# Configuration for MySQL connection
config = {
    'user': 'root',
    'password': '*********',
    'host': 'localhost'
}

try:
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database alx_book_store created successfully or already exists.")
    
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_DB_CREATE_EXISTS:
        print("Database alx_book_store already exists.")
    else:
        print(f"Failed creating database: {err}")
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals():
        connection.close()
