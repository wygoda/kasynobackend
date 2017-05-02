from django.http import JsonResponse
from . import userapi


def slot(request):
	col1 = request.POST.get('col1')
	col2 = request.POST.get('col2')
	col3 = request.POST.get('col3')
	betamount = request.POST.get('betamount')
	if col1[1]==col2[1]==col3[1]:#jesli srodkowy wiersz ma 3 takie same znaczki
		if col1[1]==1:#winogorona x2
			betamount=betamount*2
		if col1[1]==2:#wisnie x3
			betamount=betamount*3
		if col1[1]==3:#banany x4
			betamount=betamount*4
		if col1[1]==4:#gruszki x6
			betamount=betamount*6
		if col1[1]==5:#pomarancze x10
			betamount=betamount*10
		if col1[1]==6:#serduszka x15
			betamount=betamount*15
		if col1[1]==7:#monety x20
			betamount=betamount*20
		if col1[1]==8:#jackpot x30
			betamount=betamount*30
	else: #przegrana
		betamount=-betamount
	#callModifyBalance(request,betamount)
	return JsonResponse({'amount':betamount})
	
	return JsonResponse({"status":"Slots not implemented"})
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

	
	
	
def callModifyBalance(request,betamount):
	mutable = request.POST._mutable
	request.POST._mutable = True
	request.POST['amount'] = betamount
	request.POST._mutable = mutable
	response=userapi.modifyBalance(request)