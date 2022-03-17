import socket
import mariadb
import sys
inp1 = input("What is the host IP address (not port)")
inp2 = input("what is the port?")

socketSetup(inp1, inp2)

s=socket.socket()
connected = bool

def socketSetup(host,port):
    socket.gethostname()
    port = 3309
    s.bind((host,port))
    s.listen(10)
    c, addr = s.accept()

        print("Client connected, " + addr)
        content = c.recv(100).decode("UTF-8")


#initiate mariadb
conn = mariadb.connect(
    user="root",
    password="a",
    host="localhost",
    port=3306)

#declaring our cursor
cur = conn.cursor()

try:
    cur.execute(
    "SHOW columns FROM accounts.accounts ;")
