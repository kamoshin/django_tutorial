from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #output = ', '.join([q.question_text for q in latest_question_list])
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)

# def subview(request, number):
#     urlName = reverse('suburl', args=[number])
#     return HttpResponse("これはsubViewデス{0} url={1}".format(number, urlName))

def detail(request, question_id):
    return HttpResponse("You're lokking at question %s." % question_id)

def results(request, question_id):
    response = "You're lokking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
