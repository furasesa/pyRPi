import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind(("", 2303))

sock.listen(1)
print('Socket now listening')
while True:
    connection, client_addr = sock.accept()
    data = 'mode = GPIO.BCM'
    sock.sendall(data.encode("utf8"))
    break
connection.close()