from django.shortcuts import render
from django.http import HttpResponse

def welcome(request):
    return HttpResponse("<html><body>welcome to Django World</body></html>")

