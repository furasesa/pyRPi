import socket      
import json                                   

class ServerSocket:
    def __init__(self,port):
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serversocket.bind(('', port)) # host, port
    def start(self,bool_start):
        self.serversocket.listen(1)
        while bool_start:
            clientsocket,addr = self.serversocket.accept()
            dictmsg = {'test':1, 'dict':{1:2, 3:4}, 'list': [42, 16]}
            msg = json.dumps(dictmsg).encode('utf-8')
            clientsocket.send(msg)
            clientsocket.close()

if __name__=='__main__':
    s = ServerSocket(2303)
    s.start(True)


# # create a socket object
# serversocket = socket.socket(
# 	        socket.AF_INET, socket.SOCK_STREAM) 

# # get local machine name
# host = ''                         

# port = 2303                                           

# # bind to the port
# serversocket.bind((host, port))                                  

# # queue up to 1 requests
# serversocket.listen(1)                                           

# while True:
#    # establish a connection
#    clientsocket,addr = serversocket.accept()      

#    print("Got a connection from %s" % str(addr))
    
#    msg = 'Thank you for connecting'+ "\r\n"
#    clientsocket.send(msg.encode('utf-8'))
#    clientsocket.close()