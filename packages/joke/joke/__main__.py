import pyjokes
import psycopg2
import os

def main(args):
    # PostgreSQL connection string (you might want to get this from env vars)
    conn_str = "postgresql://doadmin:AVNS_VSGbT6K2T6WSOZQvp_0@db-postgresql-sgp1-03058-do-user-16324282-0.h.db.ondigitalocean.com:25060/defaultdb?sslmode=require"

    # Connect to the PostgreSQL database
    conn = psycopg2.connect(conn_str)
    cursor = conn.cursor()

    # Example query: get current time from DB
    cursor.execute("SELECT NOW()")
    current_time = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    # Your joke
    joke = pyjokes.get_joke()

    return {
        'body': {
            'response_type': 'in_channel',
            'text': f"{joke}\n\nCurrent DB time: {current_time}"
        }
    }
