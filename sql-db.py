import pandas as pd
from mysql.connector import Error
import mysql.connector


def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            database="TestDB",
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error:`{err}`")


# Create table
create_movie_table = """
    CREATE TABLE movie (
        title VARCHAR(20) PRIMARY KEY,
        year INT NOT NULL
    );
"""

# Populate movie table
pop_movie = """
    INSERT INTO movie VALUES
    ('Dune', '2015');
"""

connection = create_server_connection("localhost", "root", "password")
execute_query(connection, pop_movie)
