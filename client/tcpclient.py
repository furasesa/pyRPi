from tcptest import SocketHandler

s = SocketHandler()
s.connect('192.168.43.40',2303)

s.send('test python socket tcp port 2303')