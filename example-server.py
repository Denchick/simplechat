#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import sys

HOST = '' # Symbolic name meaning all available interfaces
PORT = 5000 # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

try:
	s.bind((HOST, PORT))
except socket.error:
	print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
	sys.exit()

print('Socket is complete')

s.listen(10)
print('Socket now listening')

# Now keep talking with the client
while True:	
	#wait to accept a connection - blocking call
	conn, addr = s.accept()
	#display client information
	print('Connected with ' + addr[0] + ':' + str(addr[1]))

	data = conn.recv(1024)
	reply = 'OK...' + data.decode()
	if not data:
		break
	
	conn.sendall(data)

conn.close()
s.close()
