#!/usr/bin/python3

import socket

serverIp = 'targetIp'
serverPort = 12345
timeoutSecs = 2.0

s = socket.socket()
s.connect((serverIp,serverPort))
s.settimeout(timeoutSecs)
while True:
    str = input("Command: ")
    s.send(str.encode());
    if(str == "Bye" or str == "bye"):
        break
    try:
        print("Response: "+s.recv(1024).decode())
    except socket.timeout:
        print("Socket timeout after 2 seconds")
s.close()
