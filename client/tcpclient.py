import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
sock.connect(("localhost", 2303))

data = sock.recv(256)
msg = data.decode("utf8").rstrip()

print(msg)