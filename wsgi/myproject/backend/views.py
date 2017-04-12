from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .APIs import userapi

@csrf_exempt #those views must accept post requests from external frontends done by the rest of the team, our own validation is required to prevent from csrf attacks
def user(request):
    # out = HttpResponse()
    # out.write('<b>ok user</b>')
    # return out

    #TODO: use openshift environment variable instead of hardcoded password
    if request.method=='POST' and request.POST.get('password')=='hasl0':
        try:
            function = request.POST.get('function')
            if function==None:
                return JsonResponse ({'status':'FAIL','error':'specify a function'})

            if function=='register':
                return userapi.register(request)

            if function=='modifyBalance':
                return userapi.modifyBalance(request)

            if function=='authenticate':
                return userapi.authenticate(request)

            if function=='info':
                return userapi.info(request)

            return JsonResponse ({'status':'FAIL','error':'there\'s no such function'})
        except:
            return JsonResponse ({'status':'FAIL', 'error':'function execution went wrong'})
    else:
        return JsonResponse({'status':'FAIL', 'error':'you didn\'t use POST or didn\'t pass validation'})

@csrf_exempt
def game(request):
    out = HttpResponse()
    out.write('<b>ok game</b>')
    return out
