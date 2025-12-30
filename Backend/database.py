import mariadb
import os
import sys

def connect():
    try:
        conn = mariadb.connect(
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", "0603"),
            host=os.getenv("DB_HOST", "db"),
            port=int(os.getenv("DB_PORT", 3306)),
            database=os.getenv("DB_NAME", "moviedb"),
            autocommit=False
        )
        cur = conn.cursor()
        return cur

    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
