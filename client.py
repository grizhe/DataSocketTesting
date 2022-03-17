import socket
import hashlib

notConnected = True
while notConnected is True:
    try: socket.create_connection(('localhost',3309))
    except: None


def hasher(i):
    str(hashlib.sha256(str(inp).encode('utf-8')).hexdigest())

if not notConnected:
    #create text user query
    #have the socket instance send this information to the server, and have the server send something back.
    inp = input("Please insert your username (the usernames in the list are grizhe and cool")
    inpencrypt = hasher(inp)
    socket.send(inpencrypt)