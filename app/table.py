import psycopg2
from db import db_connect, db_cursor

def create_tables():
    command = (
        """
        CREATE TABLE test (
            test_id INTEGER PRIMARY KEY,
            test_name VARCHAR(255) NOT NULL
        );
        """
    )

    conn = db_connect()
    cur = db_cursor(conn)
    cur.execute(command)
    cur.close()
    conn.commit()
    print("done")


create_tables()