from ..models import User
from django.http import JsonResponse

def register(request):
    return JsonResponse ({'status':'register OK'})

def modifyBalance(request):
    return JsonResponse ({'status':'modifyBalance OK'})

def authenticate(request):
    return JsonResponse ({'status':'authenticate OK'})

def info(request):
    return JsonResponse ({'status':'info OK'})
