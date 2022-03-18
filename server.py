import socket
import mariadb
import sys
import threading

HEADER = 64
PORT = 3305
#this gets the ip address of our computer and sets it to the server variable
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'UTF-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

#allows us to open up to connections - declares it as an AF_INET, and specifies that we are using a stream
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#binds the socket to the address that we listed in the top portion
s.bind(ADDR)

def handle_client(conn, addr):
    print(f"[new connection] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)
        if msg == DISCONNECT_MESSAGE:
            connected = False
        print(f"{addr} : {msg}")

    conn.close()


#initiates a connection between a singular client and stores data
def start():
    s.listen()
    print(f"[listening] Server is listening on {SERVER}")
    #this will wait until a new connection to the server occurs, and stores the address in addr, and stores info in conn
    while True:
        conn, addr = s.accept()
        #when connection occurs, pass connection to handle client, give handle client the connection and address information
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        #starts thread
        thread.start()
        #shows amount of active connections (-1 because of server.)
        print(f"[active connections:] {threading.activeCount() -1}")
print("{STARTING} server is starting")
start()



#initiate mariadb
#conn = mariadb.connect(
 #   user="root",
  #  password="a",
   # host="localhost",
    #port=3306)

#declaring our cursor
#cur = conn.cursor()

#try:
 #   cur.execute(
  #  "SHOW columns FROM accounts.accounts ;")
#except: Exception



