# db.py
import psycopg2

# ---------- DATABASE ----------
conn = psycopg2.connect(
    dbname="college",
    user="postgres",
    password="meera"
)
cur = conn.cursor()