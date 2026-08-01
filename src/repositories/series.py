
from db import get_connection


def get_all_series():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT
                    s.series_id,
                    p.name,
                    s.title,
                    s.volume,
                    s.start_year
                FROM series s 
                JOIN publishers p 
                    ON s.publisher_id = p.publisher_id
                ORDER BY 
                    p.name,
                    s.title;
             """)

            return cur.fetchall()

def add_series(
    publisher_id,
    title,
    volume,
    start_year,
):
    with get_connection() as conn:
        with conn.cursor() as cur:

            cur.execute(
                """
                INSERT INTO series
                (
                    publisher_id,
                    title,
                    volume,
                    start_year
            )
            VALUES (%s, %s, %s, %s)
            RETURNING series_id;
            """,
            (
                publisher_id,
                title,
                volume,
                start_year,
                ),
            )

            return cur.fetchone()[0]

