#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import sys

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	## The above code will create a socket with the following properties ...
	## Address Family : AF_INET (this is IP version 4 or IPv4)
	## Type : SOCK_STREAM (this means connection oriented TCP protocol)
except socket.error:
	print('Failed to create socket. Error code: ' + str(msg[0]))
	print('Error message : ' + msg[1])
	sys.exit()

print('Socket Created')
	
host = 'www.google.com'
port = 80

try:
	remote_ip = socket.gethostbyname(host)
except socket.gaierror:
	# couldn't resolve
    print('Hostname could not be resolved. Exiting')
    sys.exit()
     
print('Ip address of ' + host + ' is ' + remote_ip)

## Connect to remote server

s.connect((remote_ip, port))

print('Socket Connected to ' + host + ' on ip ' + remote_ip)

## Send some data to remote server
message = b"GET / HTTP/1.1\r\n\r\n"

try:
	## set the whole string
	s.sendall(message)
except socket.error:
	##send failed
	print('Send failed')
	sys.exit()
	
print('Message send succesfully')

## Now receive data
reply = s.recv(4096)

print(reply.decode())

s.close()
