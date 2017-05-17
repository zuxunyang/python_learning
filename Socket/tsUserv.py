#!/usr/bin/env python
from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

try:
    while True:
        print 'waiting for message...'
        data, addr = udpSerSock.recvfrom(BUFSIZE)
        portNum = getservbyname('telnet')
        print 'the data come from :',addr
        udpSerSock.sendto('[%s] %s %d' % (ctime(), data, portNum) ,addr)
        print 'the data is:' , data;
except:
    udpSerSock.close()