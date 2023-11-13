import sqlite3

from constants import *


conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()


                ################################
                # Begin Add Bus Details Tables #
                ################################


def create_operator_table():
    query = f"""CREATE TABLE IF NOT EXISTS {OPERATOR_TABLE}(
                operator_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                address TEXT NOT NULL,
                phone TEXT NOT NULL UNIQUE,
                email TEXT NOT NULL UNIQUE)
                """

    cursor.execute(query)

def create_route_table():
    query = f"""CREATE TABLE IF NOT EXISTS {ROUTE_TABLE}(
                route_id INTEGER PRIMARY KEY,
                fromStation TEXT NOT NULL,
                toStation TEXT NOT NULL)
                """

    cursor.execute(query)


def create_run_table():
    query = f"""CREATE TABLE IF NOT EXISTS {RUN_TABLE}(
                bus_id INTEGER,
                running_date TEXT NOT NULL,
                available_seats TEXT NOT NULL,
                PRIMARY KEY(bus_id,running_date))
                """

    cursor.execute(query)


def create_bus_table():
    query = f"""CREATE TABLE IF NOT EXISTS {BUS_TABLE}(
                bus_id INTEGER PRIMARY KEY,
                operator_id INTEGER NOT NULL,
                route_id INTEGER NOT NULL,
                bus_type INTEGER CHECK(bus_type >= 0  AND bus_type <= 5),
                capacity INTEGER NOT NULL,
                fare INTEGER NOT NULL,
                FOREIGN KEY(operator_id) REFERENCES {OPERATOR_TABLE}(operator_id),
                FOREIGN KEY(route_id) REFERENCES {ROUTE_TABLE}(route_id))
                """

    cursor.execute(query)


#####################################################################################################


def create_all_tables():
    create_operator_table()
    create_route_table()
    create_run_table()
    create_bus_table()


if __name__ == '__main__':
   create_all_tables()
