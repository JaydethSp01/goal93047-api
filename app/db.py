import os
import psycopg

DATABASE_URL = os.environ.get("DATABASE_URL")

try:
    conn = psycopg.connect(DATABASE_URL)
except Exception as e:
    print("Failed to connect to the database, using in-memory mock.", e)
    conn = None

def get_db():
    return conn