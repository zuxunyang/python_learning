#!/usr/bin/env python

from socket import *
import os
from time import ctime

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

serSock = socket(AF_INET, SOCK_STREAM)
serSock.bind(ADDR)
serSock.listen(5)

try:
    while True:
        print 'waiting for connection'
        serSock, addr = serSock.accept()
        print '...connection from :', addr

        while True:
            data = serSock.recv(BUFSIZE)
            os_name = os.name
            daytime = getservbyname('telnet')
            print os_name, data
            serSock.send('[%s] %s' % (ctime(),data))
        serSock.close()
except OSError:
    serSock.close()