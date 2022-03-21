import mariadb

conn = mariadb.connect(
    user="root",
    password="a",
    host="localhost",
    port=3306)

cur = conn.cursor()
type = 'username'
print(cur.execute("SELECT username FROM accounts.accounts"))