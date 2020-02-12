from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('doce de leite')

def doce1(request):
    return HttpResponse('novo doce')

def doce2(request):
    return HttpResponse('leite com goiaba')

def doce3(request):
    return HttpResponse('ainda tem doce')

def doce4(request):
    return HttpResponse('Gabriel S. Rocha')