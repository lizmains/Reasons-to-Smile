import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def select_all_emails(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM emails")

    cols = cur.fetchall()

    for col in cols:
        print(col)


def main():
    database = r"C:\Users\lizar\PycharmProjects\flaskProject\user.db"

    # create a database connection
    conn = create_connection(database)
    with conn:

        print("Pull all emails")
        select_all_emails(conn)


if __name__ == '__main__':
    main()