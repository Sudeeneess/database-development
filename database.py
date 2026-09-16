import psycopg2
from config import DB_NAME, DB_HOST, DB_PORT, DB_USER, DB_PASS

def get_connection():
    return psycopg2.connect(
        dbname=DB_NAME,
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        port=DB_PORT
    )