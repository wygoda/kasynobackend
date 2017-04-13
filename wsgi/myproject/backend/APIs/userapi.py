from ..models import User
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

def register(request):
    username = request.POST.get('username')
    exists = User.objects.filter(username=username)
    if exists: #zwraca true jesli lista nie jest pusta, false w przeciwnym wypadku
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
    userId = request.POST.get('id')
    amount = request.POST.get('amount')
    if userId==None or amount==None:
        return JsonResponse({
        'status':'FAIL',
        'function':'modifyBalance',
        'error':'there\'s no such user or invalid amount'})
    try:
        failed = 1
        u = User.objects.get(pk=userId)
        failed = u.modifyBalance(amount)
        if not failed:
            return JsonResponse({
            'status':'OK',
            'function':'modifyBalance',
            'user':str(u)})
        return JsonResponse({
        'status':'FAIL',
        'function':'modifyBalance',
        'error':'invalid amount'})
    except ObjectDoesNotExist:
        return JsonResponse({
        'status':'FAIL',
        'function':'modifyBalance',
        'error':'there\'s no such user'})

def authenticate(request):
    password = request.POST.get('userPassword')
    userId = request.POST.get('id')
    try:
        u = User.objects.get(pk=userId)
        failed = 1
        failed = u.authenticate(password)
        if not failed:
            return JsonResponse({
            'status':'OK',
            'function':'authenticate'
            })
        return JsonResponse({
        'status':'FAIL',
        'function':'authenticate',
        'error':'wrong password'
        })
    except ObjectDoesNotExist:
        return JsonResponse({
        'status':'FAIL',
        'function':'authenticate',
        'error':'there\'s no such user'})

def getAll(request):
    usersdict = {}
    for u in User.objects.all():
        usersdict[u.id] = str(u)
    return JsonResponse({
    'status':'OK',
    'function':'getAll',
    'users':usersdict})

def getUser(request):
    userId = request.POST.get('id')
    if userId==None:
        return JsonResponse({
        'status':'FAIL',
        'function':'getUser',
        'error':'there\'s no such user'})
    try:
        u = User.objects.get(pk=userId)
        return JsonResponse({
        'status':'OK',
        'function':'getUser',
        'user':str(u)})
    except ObjectDoesNotExist:
        return JsonResponse({
        'status':'FAIL',
        'function':'getUser',
        'error':'there\'s no such user'})

def delete(request):
    userId = request.POST.get('id')
    if userId==None:
        return JsonResponse({
        'status':'FAIL',
        'function':'delete',
        'error':'there\'s no such user'})
    try:
        u = User.objects.get(pk=userId)
        u.delete()
        return JsonResponse({
        'status':'OK',
        'function':'delete'})
    except ObjectDoesNotExist:
        return JsonResponse({
        'status':'FAIL',
        'function':'delete',
        'error':'there\'s no such user'})
