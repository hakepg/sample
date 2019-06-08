from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def Hello(request):
    # text = '<h1>Welcome to my app..!!</h1>'
    # return HttpResponse(text)

def hello(request):
    return render(request, 'myapp/templates/hello.html',{})