from db import get_connection


def main():
    conn = get_connection()

    with conn.cursor() as cur:
        cur.execute("SELECT * FROM publishers;")

        for publisher in cur.fetchall():
            print(publisher)

    conn.close()

    if__name__ == "__main__"
    main
