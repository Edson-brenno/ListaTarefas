from django.shortcuts import render, HttpResponse

# Create your views here.

def index(requests):

    return HttpResponse('<h1>Olá</h1>')
