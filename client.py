import socket
import hashlib

HEADER = 64
PORT = 3305
FORMAT = 'UTF-8'
DISCONNECET_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(msg)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

send('hello')

def hasher(i):
    str(hashlib.sha256(str(i).encode('utf-8')).hexdigest())