from tcptest import MySocket

s = MySocket()
s.connect('192.168.43.40',2303)

s.mysend('test python socket tcp port 2303')