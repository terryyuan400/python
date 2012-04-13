#!/usr/bin/env python

import socket
from time import ctime

HOST = ''
PORT = 23456
BUFFERSIZE = 1024
ADDR = (HOST, PORT)

serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSock.bind(ADDR)
serverSock.listen(5)

while True:
    print "wait for connection..."
    clientSock,addr = serverSock.accept()
    print "connect from:",addr
    
    while True:
        data = clientSock.recv(BUFFERSIZE)
        if not data:
            break
        clientSock.send('[%s] %s' %(ctime(),data))

serverSock.close()
clientSock.close()

