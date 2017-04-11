from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt #those views must accept post requests from external frontends done by the rest of the team, our own validation is required to prevent from csrf attacks
def user(request):
    out = HttpResponse()
    out.write('<b>ok user</b>')
    return out

@csrf_exempt
def game(request):
    out = HttpResponse()
    out.write('<b>ok game</b>')
    return out
