from django.http import HttpResponse
from django.shortcuts import render

def view_main(req):
    name = 'Lucas'
    return HttpResponse(f'<h1>Hello {name}</h1>')

user_datas = [[1, '大哥'], ['2', '二哥']]

def view_register(req):
    username = req.POST.get('user_name')
    password = req.POST.get('user_password')
    if username and password:
        user_datas.append([username, password])
    
    return render(req, 'index.html',{"datas": user_datas})