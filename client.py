import hashlib
server = 'hi'
print(f"hello, and {server}.")



def hasher(i):
    str(hashlib.sha256(str(i).encode('utf-8')).hexdigest())