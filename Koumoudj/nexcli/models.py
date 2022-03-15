# from django.db import models

# Create your models here.

import socket

class ClientQueueManager:
	@staticmethod
	def send_message(msg, ip='localhost', port=8888):
		# global ip
		# global port
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
			sock.connect((ip, port))
			sock.sendall(bytes(msg, 'utf-8'))
			response = str(sock.recv(1024), 'utf-8')
			return response

	@staticmethod
	def add_client():
		return ClientQueueManager.send_message('ADD_CLIENT')

	@staticmethod
	def add_pregnant():
		return ClientQueueManager.send_message('ADD_PREGNANT')

	@staticmethod
	def add_senior():
		return ClientQueueManager.send_message('ADD_SENIOR')

	@staticmethod
	def pop_first_client():
		return ClientQueueManager.send_message('POP_FIRST')

	@staticmethod
	def get_queue_length():
		return ClientQueueManager.send_message('COUNT')

	@staticmethod
	def get_all_clients():
		return ClientQueueManager.send_message('GET_ALL')
