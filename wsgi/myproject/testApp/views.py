from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    if request.method == 'GET':
        return HttpResponse("Hello, world. You're at the polls index and you used the GET method. hehe")
    if request.method == 'POST':
        return HttpResponse("Hello, world. You're at the polls index and you used the POST method.")
# Create your views here.
