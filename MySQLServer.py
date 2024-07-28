import mysql.connector
from mysql.connector import errorcode

config = {
    'user': 'root',
    'password': '******',
    'host': 'localhost'
}

try:
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS alx_book_store")
        cursor.execute(f"USE alx_book_store")
        cursor.execute("SELECT DATABASE()")
        current_db = cursor.fetchone()
        if current_db and current_db[0] == "alx_book_store":
            cursor.execute(f"SHOW TABLES LIKE 'dummy_table'")
            if cursor.fetchone() is None:
                print(f"Database 'alx_book_store' created successfully!")
            else:
                print(f"Database 'alx_book_store' already exists.")
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")
        exit(1)

    cursor.close()
    cnx.close()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)

