from db import get_connection

def get_all_publishers():
    """Return all publishers sorted alphabetically."""

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT publisher_id, name 
                FROM publishers 
                ORDER BY name;
            """)
            return cur.fetchall()

def add_publisher(name):
    """Insert a new publisher."""

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO publishers (name)
                VALUES (%s)
                RETURNING publisher_id;
                """,
                (name,)
            )

            return cur.fetchone()[0]
