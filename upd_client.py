#!/usr/bin/env python
# Copyright (C) 2013, Tencent
# All rights reserved.
#
# Filename   : client_udp.py
# Description: First draft
# Author     : lanceqli@tencent.com
# Version    : 1.0
# Date       : 2015-04-19
import socket
import os
import stat
import struct
import sys

class UdpClient(object):
    def send(self, ip, port, text):
        clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        sendDataLen = clientSock.sendto(text, (ip, port))
        print "sendDataLen: ", sendDataLen
        recvData = clientSock.recvfrom(1024)
        print "recvData: ", recvData

        clientSock.close()

def read_file(filename):
    file_object = open(filename, "rb")
    try:
        file_text = file_object.read( )
    finally:
        file_object.close( )
    return file_text;

def showUsage():
    print usage
    sys.exit(1)

if __name__ == '__main__':
    usage='''
    usage: ./client_udp.py <ip> <port> <data_file>
    '''
    #if len(sys.argv) != 4:
    #    showUsage()

    server_ip = "183.60.15.170"     #sys.argv[1];
    server_port = 14000             # sys.argv[2];
    filename = "wns_free_pkg_wns"   #sys.argv[3];
    print "sendto:%s:%d with %s" %(server_ip, server_port, filename);

    file_text = read_file(filename);
    udpClient = UdpClient();
    udpClient.send(server_ip, server_port, file_text);
