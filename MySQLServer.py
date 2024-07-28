#!/usr/bin/python3
# MySQLServer.py

import mysql.connector
from mysql.connector import Error

def create_database(db_name):
    try:
        # Establish a connection to the MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='your_username',
            password='your_password'
        )

        if connection.is_connected():
            # Create a cursor object
            cursor = connection.cursor()

            # Create the database if it doesn't already exist
            create_db_query = f"CREATE DATABASE IF NOT EXISTS `{db_name}`"
            cursor.execute(create_db_query)

            # Commit the changes
            connection.commit()

            print(f"Database '{db_name}' created successfully!")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            # Close the cursor and connection
            cursor.close()
            connection.close()

if __name__ == "__main__":
    db_name = 'alx_book_store'
    create_database(db_name)
