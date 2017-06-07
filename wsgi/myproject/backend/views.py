from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .APIs import userapi
from .APIs import games
from .APIs import checkapi
import os
import json

@csrf_exempt #these views must accept post requests from external frontends done by the rest of the team, our own validation is required to prevent from csrf attacks
def user(request):
	# out = HttpResponse()
	# out.write('<b>ok user</b>')
	# return out
	jsonObj = userapi.authenticate(request)
	return JsonResponse ({'jsonObj':jsonObj.content})
	
	#if request.method=='POST':
	#	try:
	#		function = request.POST.get('function')
	#		if function==None:
	#			return JsonResponse ({'status':'FAIL','error':'specify a function'})
    #
	#		if function=='register':
	#			return userapi.register(request)
    #
	#		if function=='modifyBalance':
	#			return userapi.modifyBalance(request)
    #
	#		if function=='authenticate':
	#			return userapi.authenticate(request)
    #
	#		if function=='getAll':
	#			return userapi.getAll(request)
    #
	#		if function=='getUser':
	#			return userapi.getUser(request)
    #
	#		if function=='delete':
	#			return userapi.delete(request)
    #
	#		return JsonResponse ({'status':'FAIL','error':'there\'s no such function'})
	#	except:
	#		return JsonResponse ({'status':'FAIL', 'error':'function execution went wrong'})
	#else:
	#	return JsonResponse({'status':'FAIL', 'error':'you didn\'t use POST or didn\'t pass validation'})

@csrf_exempt
def game(request):
	if request.method=='POST' and request.POST.get('password')==os.environ.get('apiPassword'):
		try:
			function = request.POST.get('function')
			if function==None:
				return JsonResponse ({'status':'FAIL','error':'specify a function'})
			if function=='slot':
				return games.slot(request)
			if function=='roulette':
				return games.roulette(request)
			if function=='dice':
				return games.dice(request)
			if function=='blackjack':
				return games.blackjack(request)
			if function=='poker':
				return games.poker(request)
			if function=='baccarat':
				return games.baccarat(request)
			if function=='cointoss':
				return games.cointoss(request)
			else:
				return JsonResponse({"error":"There is no such function"})
		except:
			return JsonResponse ({'status':'FAIL', 'error':'function execution went wrong'})
	else:
		return JsonResponse({'status':'FAIL', 'error':'you didn\'t use POST or didn\'t pass validation'})
		
		
@csrf_exempt
def check(request):
	if request.method=='POST' and request.POST.get('password')==os.environ.get('apiPassword'):
		function = request.POST.get('function')
		if function==None:
			return JsonResponse ({'status':'FAIL','error':'specify a function'})
		if function=='slot':
			return checkapi.slot(request)
		if function=='roulette':
			return checkapi.roulette(request)
		if function=='dice':
			return checkapi.dice(request)
		if function=='blackjack':
			return checkapi.blackjack(request)
		if function=='poker':
			return checkapi.poker(request)
		if function=='baccarat':
			return checkapi.baccarat(request)
		if function=='cointoss':
			return checkapi.cointoss(request)
		else:
			return JsonResponse({"error":"There is no such function"})