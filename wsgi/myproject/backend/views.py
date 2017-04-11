from django.shortcuts import render
from django.http import HttpResponse, Http404

def user(request):
    out = HttpResponse()
    out.write('<b>ok</b>')
    return out
