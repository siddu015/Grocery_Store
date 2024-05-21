import mysql.connector

__cnx = None

def get_sql_connection():
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(user='root', password='pass5678',
                                        host='localhost',
                                        database='Grocery_Store')

    return __cnx
