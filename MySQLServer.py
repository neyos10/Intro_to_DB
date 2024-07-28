import mysql.connector

def create_database():
    try:
        cnx = mysql.connector.connect(
            user='root',
            password='inyass-08131307070.24434',
            host='localhost'
        )
        cursor = cnx.cursor()
        
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if cnx.is_connected():
            cursor.close()
            cnx.close()

if __name__ == "__main__":
    create_database()
