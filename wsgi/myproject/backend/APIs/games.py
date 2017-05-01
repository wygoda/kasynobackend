from django.http import JsonResponse

def slot(request):
	return JsonResponse({
	'status':'FAIL',
	'error':'Slot machines are not implemented yet'})
def roulette(request):
	return JsonResponse({
	'status':'FAIL',
	'error':'Roulette is not implemented yet'})
def dice(request):
	return JsonResponse({
	'status':'FAIL',
	'error':'Dices are not implemented yet'})
def blackjack(request):
	return JsonResponse({
	'status':'FAIL',
	'error':'Blackjack is not implemented yet'})
def poker(request):
	return JsonResponse({
	'status':'FAIL',
	'error':'Poker is not implemented yet'})
def baccarat(request):
	return JsonResponse({
	'status':'FAIL',
	'error':'Baccarat is not implemented yet'})