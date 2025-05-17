from django.contrib import auth
from django.shortcuts import redirect, render

def login(request):
    if request.user.is_authenticated:
        return redirect('announcementList')
    data = {}
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = auth.authenticate(username = username, password = password)
        if user is None:
            data['msg'] = "登入失敗"
        else:
            auth.login(request, user)

    return render(request, 'announcement/login.html', data)