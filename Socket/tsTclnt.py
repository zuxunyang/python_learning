#!/usr/bin/env python

from socket import *

DEFAULT_HOST = 'localhost'
DEFAULT_PORT = 21567
BUFSIZE = 1024
DEFAULT_ADDR = (DEFAULT_HOST, DEFAULT_PORT)

host = raw_input("please input host:")
port = int(raw_input("please input port:"))

if host is not None and port is not None:
    ADDR = (host, port)
else:
    ADDR = DEFAULT_ADDR

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

try:
    while True:
        data = raw_input('> ')
        if not data:
            break
        tcpCliSock.send(data)
        data = tcpCliSock.recv(BUFSIZE)
        if not data:
            break
        print data
except KeyboardInterrupt:
    tcpCliSock.close()