from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    if request.method == 'GET':
        return HttpResponse("Hello, world. You're at the polls index and you used the GET method. hehe3")
    if request.method == 'POST':
        return HttpResponse("Hello, world. You're at the polls index and you used the POST method.")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
