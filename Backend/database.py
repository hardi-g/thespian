import mariadb
import sys

def connect():
    try:
        conn = mariadb.connect(
            user="root",
            password="0603",
            host="localhost",
            port=3306,
            database="moviedb",
            autocommit = False
        )
        cur = conn.cursor()
        return cur
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)