from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def calculate(x, y):
    return x + y


def say_hello(request):
    res = calculate(10, 20)
    return render(request, 'hello.html', {'name': 'Aida'})
