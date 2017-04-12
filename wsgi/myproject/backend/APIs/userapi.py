from ..models import User
from django.http import JsonResponse

def register(request):
    username = request.POST.get('username')
    exists = User.objects.filter(username=username)
    if exists:
        return JsonResponse({
        'status':'FAIL',
        'function':'register',
        'error':'username already exists'})
    password = request.POST.get('userPassword')

    if username==None or password==None or username=='' or password=='':
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
    return JsonResponse({'status':'OK'})

def authenticate(request):
    return JsonResponse({'status':'OK'})

def info(request):
    usersdict = {}
    for u in User.objects.all():
        usersdict[u.id] = str(u)
    return JsonResponse({
    'status':'OK',
    'function':'info',
    'users':usersdict})

def delete(request):
    pass
