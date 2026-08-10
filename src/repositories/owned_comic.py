
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
