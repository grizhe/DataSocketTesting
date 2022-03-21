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

def userCreator(username, password, secnum):
    cur.execute(
    "INSERT INTO accounts(username, password, secnum) VALUES ('" + username + "', '" + password + "', '" + int(secnum) + "');"
    )
    conn.commit()

userCreator('grizheman', 'hihihi', '12345')