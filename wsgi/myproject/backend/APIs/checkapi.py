from django.http import JsonResponse


def slot(request):
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
