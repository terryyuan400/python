#!/usr/bin/env python

import socket
import time

HOST = 'localhost'
PORT = 23456
BUFFERSIZE = 1024
ADDR = (HOST, PORT)

clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSock.connect(ADDR)

while True:
    data = raw_input(">")
    if not data:
        break

    clientSock.send(data)

    datafromserver = clientSock.recv(BUFFERSIZE)
    if not datafromserver:
        break

    print datafromserver

clientSock.close()
