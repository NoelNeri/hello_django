from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} que tem {} anos !!! Tudo Bom??</h1>'.format(nome,idade))

def soma(request, val1, val2):
    return HttpResponse('<h1>A soma de {} e {} resulta em {}.</h1>'.format(val1, val2, val1+val2))

def subt(request, val1, val2):
    return HttpResponse('<h1>A subtracao de {} do valor {} resulta em {}.</h1>'.format(val1, val2, val2-val1))

def multi(request, val1, val2):
    return HttpResponse('<h1>A multiplicacao de {} por {} resulta em {}.</h1>'.format(val1, val2, val1*val2))

def divi(request, val1, val2):
    return HttpResponse('<h1>A divisao de {} por {} resulta em {}.</h1>'.format(val1, val2, val1/val2))
