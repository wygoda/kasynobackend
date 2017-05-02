from django.http import JsonResponse
from . import userapi


def slot(request):
	mid1 = request.POST.get('mid1')
	mid2 = request.POST.get('mid2')
	mid3 = request.POST.get('mid3')
	betamount = int(request.POST.get('betamount'))
	if mid1==mid2==mid3:#jesli srodkowy wiersz ma 3 takie same znaczki
		if mid1=='1':#winogorona x2
			betamount=betamount*2
		if mid1=='2':#wisnie x3
			betamount=betamount*3
		if mid1=='3':#banany x4
			betamount=betamount*4
		if mid1=='4':#gruszki x6
			betamount=betamount*6
		if mid1=='5':#pomarancze x10
			betamount=betamount*10
		if mid1=='6':#serduszka x15
			betamount=betamount*15
		if mid1=='7':#monety x20
			betamount=betamount*20
		if mid1=='8':#jackpot x30
			betamount=betamount*30
	else: #przegrana
		betamount=-betamount
	callModifyBalance(request,betamount)
	return JsonResponse({
	'amount':betamount,
	'result':mid1==mid2==mid3,
	'result2':mid1==1,
	'result3':mid1=='1',
	'mid1':mid1,
	'mid2':mid2,
	'mid3':mid3,
	})
	
def roulette(request):
	return JsonResponse({"status":"Roulette not implemented"})
def dice(request):
	return JsonResponse({"status":"Dices not implemented"})
def blackjack(request):
	return JsonResponse({"status":"Blackjack not implemented"})
def poker(request):
	return JsonResponse({"status":"Poker not implemented"})
def baccarat(request):
	return JsonResponse({"status":"Baccarat not implemented"})
def cointoss(request):
	return JsonResponse({"status":"Coin toss not implemented"})

	
	
	
def callModifyBalance(request,amount):
	mutable = request.POST._mutable
	request.POST._mutable = True
	request.POST['amount'] = amount
	request.POST._mutable = mutable
	response=userapi.modifyBalance(request)