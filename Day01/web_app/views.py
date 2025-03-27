from django.http import HttpResponse
from django.shortcuts import render

def view_main(req):
    name = 'Lucas'
    return HttpResponse(f'<h1>Hello {name}</h1>')

def view_list(req):
    return render(req, 'index.html')