from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
# from django.template import loader

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('testApp/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    # out = HttpResponse()
    # for key in request.META:
    #     out.write('<b>' + str(key) + '</b>' + ':' + str(request.META[key]) + '<br/>')
    #
    # return HttpResponse(out)
    return render(request, 'testApp/index.html', context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'testApp/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
