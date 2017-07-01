import math
from socket import socket
from random import randint
from numpy import random
from threading import Thread

class Server:

	LEVEL_SIZES = [2, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8]
	def __init__(self, port = 2222, listen_amount = 5):
		self.sock = socket()
		self.sock.bind(('0.0.0.0', port))
		self.sock.listen(listen_amount)
		self.clients = []
		self.level_size_index = 0
		self.levels = []

	def accept_clients(self):
		while True:
			client_sock, client_addr = self.sock.accept()
			self.clients.append(client_sock)
			t = Thread(target = self.handle_client, args = (client_sock, ))
			t.start()

	def handle_client(self, client):
		level_index = 0
		while True:
			if level_index >= len(self.levels):
				self.levels.append(self.create_level())

			client.send(str(self.levels[level_index]))

			success = client.recv(1)

			level_index += 1

	def create_level(self):
		level_size = Server.LEVEL_SIZES[self.level_size_index]
		if self.level_size_index < len(Server.LEVEL_SIZES) - 1:
			self.level_size_index += 1

		main_color = randint(0, 0xffffff)
		other_color = int(random.normal(main_color, 5))

		while math.fabs(other_color - main_color) < 80 and math.fabs(other_color - main_color) > 60:
			other_color = int(random.normal(main_color, 5))

		main_color = hex(main_color)
		other_color = hex(other_color)

		return (level_size, main_color, other_color)



s = Server()
s.accept_clients()
