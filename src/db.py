import psycopg

def get_connection():
    """Create and return a connection to the comic database"""
    return psycopg.connect(
        dbname="comic_db",
        user="michael",
    )
