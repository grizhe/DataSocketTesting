import mariadb

conn = mariadb.connect(
    user="root",
    password="a",
    host="localhost",
    port=3306,
    database="accounts")

cur = conn.cursor()

print(cur.execute("SELECT username FROM accounts"))
for user in cur:
    print(user)

joshUser = 'jw'
jpass = 'pass'

cur.execute(f"INSERT INTO accounts (username, password) VALUES ({joshUser}, {jpass})")
conn.commit()