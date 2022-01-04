# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def calculator(request):
    return HttpResponse("Hello, world. You're at the polls index.")
