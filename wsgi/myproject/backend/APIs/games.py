from django.http import JsonResponse
from random import sample

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
	cards=sample(range(1,53),10)
	return JsonResponse({
	"cards":cards})
def baccarat(request):
	return JsonResponse({
	'status':'FAIL',
	'error':'Baccarat is not implemented yet'})