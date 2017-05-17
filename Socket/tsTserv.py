#!/usr/bin/env python

from socket import  *
from time import ctime


HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)
while True:
    print 'waiting for connection...'
    tcpSerSock, addr = tcpSerSock.accept()
    print '...connected from:', addr

    while True:
        data = tcpSerSock.recv(BUFSIZE)
        if not data:
            break
        print 'the data is:', data
        tcpSerSock.send('[%s] %s' % (ctime(), data))
    tcpSerSock.close()

tcpSerSock.close()

