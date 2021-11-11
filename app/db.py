import psycopg2
import psycopg2.extras

DB_HOST = "localhost"
DB_NAME = "ujicoba"
DB_USER = "postgres"
DB_PASS = "pass"

# Koneksi ke database
def db_connect():
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
    return conn

# Cursor - gatau pokonya kalo mau ngambil data harus pake cursor
# didalem kurungnya harus ada nilai yang dimasukin
# link https://www.psycopg.org/docs/cursor.html
def db_cursor(conn):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    return cur



