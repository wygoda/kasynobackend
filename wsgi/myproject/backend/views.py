from django.shortcuts import render
from django.http import HttpResponse, Http404

def user(request):
    out = HttpResponse()
    out.write('<b>ok user</b>')
    return out

def game(request):
    out = HttpResponse()
    out.write('<b>ok game</b>')
    return out
