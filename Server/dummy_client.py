from socket import socket
from time import sleep

s = socket()
s.connect(('127.0.0.1', 2222))
while 1:
	print s.recv(4096)
	sleep(1)
	s.send('k')
