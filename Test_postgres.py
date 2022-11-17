import psycopg2 

conn = psycopg2.connect(
    host="Aquiles",
    database="testdb",
    user="monitor",
    password="Emilita01")


cur = conn.cursor()
cur.execute('SELECT version()')
db_version = cur.fetchone()
print(db_version)
