#!/usr/bin/env python

from socket import *
import os
from time import ctime

HOST = 'localhost'
PORT= 21567
BUFSIZE = 1024

ADDR = (HOST, PORT)

cliSock = socket (AF_INET, SOCK_STREAM)
cliSock.connect(ADDR)

try:
    while True:
        data = raw_input('> ')
        if not data:
            break
        os_name = os.name
        ld = os.listdir('/usr')
        cliSock.sendto ('[%s] %s %s %s' % (ctime(), os_name, ld, data),ADDR)
        data = cliSock.recv(BUFSIZE)
        if not data:
            break
        print data
except OSError:
    cliSock.close()