from django.shortcuts import render, redirect
from django.http import HttpResponse

# from . import models
from .models import ClientQueueManager

def index(request):
	if('login' in request.session):
		return HttpResponse(" ... Home ...")
	else:
		return auth(request)

def auth(request):
	return HttpResponse(" Authentification : give your login and password")

def ticket(request, client_type): # client_type \in [ c, p, s ]
	if(not client_type in ['c', 'p', 's']):
		return index(request)
	elif(client_type == 'c'):
		response = ClientQueueManager.add_client()
		return HttpResponse(" Added client : " + response)
	elif(client_type == 'p'):
		response = ClientQueueManager.add_pregnant()
		return HttpResponse(" Added pregnant : " + response)
	elif(client_type == 's'):
		response = ClientQueueManager.add_senior()
		return HttpResponse(" Added senior : " + response)

def caisse(request):
	if('guichet' in request.session):
		response = ClientQueueManager.pop_first_client()
		return HttpResponse(" Carry client (" + response + ") at Guichet " + str(request.session['guichet']))
	else:
		return guichet(request)

def guichet(request):
	pass

def show(request):
	response = ClientQueueManager.get_all_clients()
	return HttpResponse(" Show queue : " + response)

def start(request):
	pass