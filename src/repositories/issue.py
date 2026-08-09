

from db import get_connection


def get_all_issues():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT
                    i.issue_id,
                    i.series_id,
                    i.issue_number,
                    i.publication_date,
                    i.is_key_issue,
                    i.variant
                FROM issues AS i 
                JOIN series AS s 
                    ON i.series_id = s.series_id
                ORDER BY 
                    s.series_id,
                    i.issue_number;
             """)

            return cur.fetchall()


def get_issues_by_series(series_id):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT
                    i.issue_id,
                    i.series_id,
                    i.issue_number,
                    i.publication_date,
                    i.is_key_issue,
                    i.variant
                FROM issues AS i 
                JOIN series AS s 
                    ON s.series_id = i.series_id
                WHERE i.series_id = %s
                ORDER BY i.issue_number;
             """, (series_id,))

            return cur.fetchall()


def add_issue(series_id, issue_number, publication_date, is_key_issue,
              variant):
    with get_connection() as conn:
        with conn.cursor() as cur:

            cur.execute(
                """
                INSERT INTO issues
                (
                    series_id,
                    issue_number,
                    publication_date,
                    is_key_issue,
                    variant
            )
            VALUES (%s, %s, %s, %s,%s)
            RETURNING issue_id;
            """,
            (
                series_id,
                issue_number,
                publication_date,
                is_key_issue,
                variant
                ),
            )

            return cur.fetchone()[0]

