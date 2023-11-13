import sqlite3

from constants import *

conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()


def create_operator_table():
    query = f"""CREATE TABLE IF NOT EXISTS {OPERATOR_TABLE}(
                operator_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                address TEXT NOT NULL,
                phone TEXT NOT NULL UNIQUE,
                email TEXT NOT NULL UNIQUE)
                """

    cursor.execute(query)

if __name__ == '__main__':
    create_operator_table()
