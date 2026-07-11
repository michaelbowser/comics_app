import psycopg

conn = psycopg.connect("dbname=comic_db user=michael")

cur = conn.cursor()

cur.execute("SELECT * FROM publishers;")
rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()
