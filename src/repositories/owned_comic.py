
from db import get_connection

def add_owned_comic(
    issue_id,
    box_id,
    grade,
    purchase_price,
    purchase_date,
    estimated_value,
    signed,
    certification_company,
    certification_number,
    notes):
    with get_connection() as conn:
        with conn.cursor() as cur:

            cur.execute(
                """
                INSERT INTO owned_comics
                (
                    issue_id,
                    box_id,
                    grade,
                    purchase_price,
                    purchase_date,
                    estimated_value,
                    signed,
                    certification_company,
                    certification_number,
                    notes
            )
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            RETURNING owned_id;
            """,
            (
                issue_id,
                box_id,
                grade,
                purchase_price,
                purchase_date,
                estimated_value,
                signed,
                certification_company,
                certification_number,
                notes,
                ),
            )

            return cur.fetchone()[0]

def get_all_owned_comics():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT
                    o.owned_id,
                    o.issue_id,
                    s.title,
                    i.issue_number,
                    i.publication_date,
                    i.is_key_issue,
                    i.variant,
                    o.box_id,
                    b.label,
                    b.location,
                    o.grade,
                    o.purchase_price,
                    o.purchase_date,
                    o.estimated_value,
                    o.signed,
                    o.certification_company,
                    o.certification_number,
                    o.notes
                FROM owned_comics AS o
                JOIN issues AS i
                    ON o.issue_id = i.issue_id
                JOIN series AS s 
                    ON i.series_id = s.series_id
                LEFT JOIN boxes AS b 
                    on o.box_id = b.box_id 
                ORDER BY o.owned_id;
            """)

            return cur.fetchall()
