from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse('Página inicial!!!')


def contacts(request):
    return HttpResponse('Página de contatos')
