import mysql.connector
from mysql.connector import errorcode

config = {
    'user': 'root',
    'password': '******',
    'host': 'localhost'
}

DB_NAME = 'alx_book_store'

try:
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        cursor.execute(f"USE {DB_NAME}")
        cursor.execute("SELECT DATABASE()")
        current_db = cursor.fetchone()
        if current_db and current_db[0] == DB_NAME:
            cursor.execute(f"SHOW TABLES LIKE 'dummy_table'")
            if cursor.fetchone() is None:
                print(f"Database '{DB_NAME}' created successfully!")
            else:
                print(f"Database '{DB_NAME}' already exists.")
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

