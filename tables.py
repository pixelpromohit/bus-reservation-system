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


def add_into_operator_table(operator_id, name, address, phone, email):
    # check if operator_id already exists
    # exists_query  = f"""SELECT *FROM {OPERATOR_TABLE} WHERE operator_id=?"""
    # exists = cursor.execute(exists_query, [(operator_id)])
    # if cursor.fetchone() != None:
    #     print(f"{operator_id} already exists in the table")
    #     return False

    try:
        query = f"""INSERT INTO {OPERATOR_TABLE}(operator_id , name , address , phone , email)
                    VALUES(? , ? , ? , ? , ?)
                    """
        cursor.execute(query, (operator_id, name, address, phone, email))
        conn.commit()
        return True
    except Exception as e:
        print(f"An error occurred= {e}")
        return False


def edit_into_operator_table(operator_id, name, address, phone, email):
    exists_query = f"""SELECT *FROM {OPERATOR_TABLE} WHERE operator_id=?"""
    exists = cursor.execute(exists_query, [(operator_id)])
    if cursor.fetchone() is None:
        print(f"operator_id = {operator_id} does not exists in the table")
        return False

    try:
        query = f""" UPDATE {OPERATOR_TABLE} SET name = ? , address = ? , phone = ? , email = ? WHERE operator_id = ?"""
        cursor.execute(query, (name, address, phone, email, operator_id))
        conn.commit()
        return True
    except Exception as e:
        print(f"An error occured while editing = {e}")
        return False


def create_route_table():
    query = f"""CREATE TABLE IF NOT EXISTS {ROUTE_TABLE}(
                route_id INTEGER PRIMARY KEY,
                fromStation TEXT NOT NULL,
                toStation TEXT NOT NULL)
                """

    cursor.execute(query)


def add_into_route_table(route_id, fromStation, toStation):
    try:
        query = f""" INSERT INTO {ROUTE_TABLE}(route_id , fromStation ,toStation)
                VALUES(? , ? , ?)"""

        cursor.execute(query, (route_id, fromStation, toStation))
        conn.commit()
        return True
    except Exception as e:
        print(f"An error occured = {e}")
        return False


def delete_from_route_table(route_id, fromStation, toStation):
    try:
        query = f"""DELETE FROM {ROUTE_TABLE} WHERE route_id = ?"""
        cursor.execute(query, (route_id,))
        conn.commit()
        return True
    except Exception as e:
        print(f"An error occured = {e}")
        return False


def create_run_table():
    query = f"""CREATE TABLE IF NOT EXISTS {RUN_TABLE}(
                bus_id INTEGER,
                running_date TEXT NOT NULL,
                available_seats TEXT NOT NULL,
                PRIMARY KEY(bus_id,running_date))
                """

    cursor.execute(query)


def insert_into_run_table(bus_id, running_date, available_seats):
    try:
        query = f""" INSERT INTO {RUN_TABLE}(bus_id , running_date , available_seats)
               VALUES(? , ? , ?)"""

        cursor.execute(query, (bus_id, running_date, available_seats))
        conn.commit()
        return True
    except Exception as e:
        print(f"An error  occured = {e}")
        return False


def delete_from_run_table(bus_id, runnning_date, available_seats):
    try:
        query = f""" DELETE FROM {RUN_TABLE} WHERE bus_id = ?"""
        cursor.execute(query, (bus_id,))
        conn.commit()
        return True
    except Exception as e:
        print(f"An error occured = {e}")
        return False


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


def insert_into_bus_table(bus_id, operator_id, route_id, bus_type, capacity, fare):
    try:
        query = f""" INSERT INTO {BUS_TABLE}(bus_id , operator_id , route_id , bus_type , capacity , fare)
                VALUES(? , ? , ? , ? , ? , ?)"""

        cursor.execute(query, (bus_id, operator_id, route_id, bus_type, capacity, fare))
        conn.commit()
        return True
    except Exception as e:
        print(f"An error occured = {e}")
        return False


def edit_into_bus_table(bus_id, operator_id, route_id, bus_type, capacity, fare):
    try:
        query = f""" UPDATE {BUS_TABLE} SET operator_id=? , route_id=? , bus_type=? , capacity=? , fare=? WHERE bus_id=?"""

        cursor.execute(query, (operator_id, route_id, bus_type, capacity, fare, bus_id))
        conn.commit()
        return True
    except Exception as e:
        print(f"An error occured = {e}")
        return False


#####################################################################################################


def create_all_tables():
    create_operator_table()
    create_route_table()
    create_run_table()
    create_bus_table()


if __name__ == "__main__":
    create_all_tables()
    # success = add_into_operator_table(
    #     5, "rohit", "pune", "8087900440", "teamrohit@gmail.com"
    # )
    # edit_into_operator_table(
    #     88, "mohit ramchandani", "mumbai", "8087900447", "gfg@gmail.com"
    # )
    # add_into_route_table(1, "guna", "bhopal")
    # add_into_route_table(1, "guna", "pune")
    # add_into_route_table(2, "guna", "mumbai")
    # delete_from_route_table(1, "guna", "bhopal")

    # insert_into_run_table(2, "3/7/2003", "4/20")
    # delete_from_run_table(3, "3/7/2003", "4/20")

    insert_into_bus_table(4, 10, 3, 2, 4, 1000)
# edit_into_bus_table(1 , 3 , 3 , 4 , 3, 200)
