import psycopg2


conn = psycopg2.connect(
    dbname="broadways",
    user="postgres",
    password="password",
    host="localhost",
    port="5432"
)
# Create a cursor object using the connection
cursor = conn.cursor()

cursor.execute("SELECT * FROM students")

rows= cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
conn.close()