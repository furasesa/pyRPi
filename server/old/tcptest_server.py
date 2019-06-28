import sys
import socket
from config import Config

class MySocket:
    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            print('Socket created')
        else:
            self.sock = sock
        try:
            self.sock.bind(("", 2303))
            print('Socket bind complete')
        except socket.error as msg:
            print('Bind failed. Error : ' + str(sys.exc_info()))
            sys.exit()
        #Start listening on socket
        self.sock.listen(1)
        print('Socket now listening')
        while True:
            connection, client_addr = self.sock.accept()
            data = 'mode = GPIO.BCM'
            self.sock.sendall(data.encode("utf8"))
            break
        connection.close()

if __name__ == '__main__':
    MySocket()
