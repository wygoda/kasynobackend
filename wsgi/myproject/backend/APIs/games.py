from django.http import JsonResponse
from random import sample,randint
from . import checkapi

def slot(request):
	col1 = [randint(1,8) for n in range(8)]
	col2 = [randint(1,8) for n in range(8)]
	col3 = [randint(1,8) for n in range(8)]
	col12 = [randint(1,8) for n in range(8)]
	col22 = [randint(1,8) for n in range(8)]
	col32 = [randint(1,8) for n in range(8)]
	return JsonResponse({
	"col1":col1,
	"col2":col2,
	"col3":col3,
	"col12":col12,
	"col22":col22,
	"col32":col32})
def roulette(request):
	return JsonResponse({"result":randint(0,36)})
def dice(request):
	throws = [randint(1,6),randint(1,6)]
	return JsonResponse({"throws":throws})
def blackjack(request):
	cards=[randint(1,52) for n in range(42)]#42 random numbers form 1 to 52
	return JsonResponse({"cards":cards})
def poker(request):
	cards=sample(range(1,53),10)#10 different random numbers form 1 to 52
	return JsonResponse({"cards":cards})
def baccarat(request):
	player = [randint(1,52) for n in range(2)]
	bank = [randint(1,52) for n in range(2)]
	#if checkapi.baccaratScore(player)>=8 or checkapi.baccaratScore(bank)>=8:
	return JsonResponse({
	'bank':bank,
	'player':player})
		
def cointoss(request):
	result = randint(0,1)
	if result == 0:
		return JsonResponse({"toss":"heads"})
	else:
		return JsonResponse({"toss":"tails"})