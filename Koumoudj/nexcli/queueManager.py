#not /usr/bin/python
# -*- coding: latin-1 -*-

import socket

from fileDattente import FileDattente
from fileDattente import Client

class ClientQueueManager:
	"""demonstration class only
	  - coded for clarity, not efficiency
	"""

	def __init__(self, port = 8888, maxNumberOfConnections = 10):
		self.port = port
		self.maxNumberOfConnections = maxNumberOfConnections
		# Création de l'objet "file d'attente"
		self.fileDattente = FileDattente()
	
	def start(self):
		# From: https://docs.python.org/fr/3/howto/sockets.html
		# create an INET, STREAMing socket
		serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# bind the socket to a public host, and a well-known port
		# serversocket.bind((socket.gethostname(), self.port))
		serversocket.bind(('localhost', self.port))
		# become a server socket
		serversocket.listen(self.maxNumberOfConnections)
		print(" -- Listening ...")
		while True:
			# accept connections from outside
			(clientSocket, address) = serversocket.accept()
			# now do something with the clientSocket
			# in this case, we'll pretend this is a threaded server
			# ss
			# ct = client_thread(clientSocket)
			# ct.run()
			while True:
				receivedData = clientSocket.recv(1024)
				if not receivedData: 
					break
				# Echo back the same data you just received
				# text = " - Response : " + str(receivedData, "utf-8")
				# clientSocket.send(" - Response : " + str(receivedData))
				# clientSocket.send(bytes(text, "utf-8"))
				self.computeCommand(clientSocket, str(receivedData, "utf-8"))
			clientSocket.close()
	
	def isBadCommand(self, command):
		if(command in ['add_client', 'add_pregnant', 'add_senior', 'pop_first', 'count', 'get_all']):
			return False
		else:
			return True
	
	def computeCommand(self, clientSocket, command):
		command = command.lower()
		if(self.isBadCommand(command)):
			clientSocket.send(bytes("0\tBad command", "utf-8"))
		else:
			print(' -- Received command : ' + command)
			if(command == 'add_client'): # Choix d'ajout d'un client dans la file d'attente
				number, arrival = self.fileDattente.addClient()
				clientSocket.send(bytes(str(number) + "\t" + arrival, "utf-8"))
			elif(command == 'add_pregnant'): # Choix d'ajout d'une cliente en état de grossesse dans la file d'attente
				number, arrival = self.fileDattente.addPregnantClient()
				clientSocket.send(bytes(str(number) + "\t" + arrival, "utf-8"))
			elif(command == 'add_senior'): # Choix d'ajout d'un client senior dans la file d'attente
				number, arrival = self.fileDattente.addSeniorClient()
				clientSocket.send(bytes(str(number) + "\t" + arrival, "utf-8"))
			elif(command == 'pop_first'): # Choix de récupération du client en tête de la file d'attente
				client = self.fileDattente.getNextClient()
				if(client != None):
					number = client.getNumber()
					arrival = client.getArrival()
					clientSocket.send(bytes(str(number) + "\t" + arrival, "utf-8"))
				else:
					clientSocket.send(bytes("0\t", "utf-8"))
			elif(command == 'count'): # Choix d'affichage du nombre de clients dans la file d'attente
				count = self.fileDattente.countNumberOfClients()
				clientSocket.send(bytes(str(count) + "\t", "utf-8"))
			elif(command == 'get_all'): # Choix d'affichage des clients de la file d'atten
				text = self.fileDattente.showQueue()
				clientSocket.send(bytes(text, "utf-8"))

server = ClientQueueManager()
server.start()
