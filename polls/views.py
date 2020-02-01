from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

def index(request):
    urlName = reverse('index')
    return HttpResponse("Hello World{0}".format(urlName))

def subview(request, number):
    urlName = reverse('suburl', args=[number])
    return HttpResponse("これはsubViewデス{0} url={1}".format(number, urlName))
# Create your views here.
