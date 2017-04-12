from ..models import User
from django.http import JsonResponse

def register(request):
    username = request.POST.get('username')
    notempty = User.objects.filter(username=username)
    if notempty:
        return JsonResponse({
        'status':'FAIL',
        'function':'register',
        'error':'username already exists'})
    password = request.POST.get('userPassword')

    if username==None or password==None:
        return JsonResponse({
        'status':'FAIL',
        'function':'register',
        'error':'username or password empty'})
    balance = request.POST.get('balance') #will return None if it doesn't find the key

    if balance==None:
        balance = 0

    u = User(username=username, password=password, balance=balance)

    try:
        u.save()
    except:
        return JsonResponse({
        'status':'FAIL',
        'function':'register',
        'error':'save() error'})

    return JsonResponse({
    'status':'OK',
    'function':'register',
    'id':u.id})

def modifyBalance(request):
    return JsonResponse ({'status':'OK'})

def authenticate(request):
    return JsonResponse ({'status':'OK'})

def info(request):
    return JsonResponse ({'status':'OK'})
