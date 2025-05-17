"""
python manage.py runserver
"""

from django.http import HttpResponse
from django.shortcuts import render
from google import genai
# from web_app.models import UserData
from ..models.userData import UserData

# Create your views here.
def view_main():
    string = "123"
    return HttpResponse("<p>django {}</p>".format(string))


userData = list()
def view_list(request):
    global userData
    userName = request.POST.get("user_name")
    userPassword = request.POST.get("user_password")
    if userName and userPassword:
        userData.append([userName, userPassword])
    print(userData)
    return render(request, "index.html", {"datas": userData})

def view_test2(request):
    data = dict()
    if request.method == "POST":
        in_name = request.POST["name"]
        in_phone = request.POST["phone"]
        in_gender = request.POST["gender"]
        in_age = request.POST["age"]

        UserData.objects.create(
            name = in_name,
            phone = in_phone,
            gender = in_gender,
            age = in_age
        )
        data['msg'] = "新增成功"
    
    data["gender_choices"] = UserData.GENDER_CHOICES

    return render(request, "index2.html", data)



chat_log = str()
chat_list = list()
def chat(request):
    gemini_api_key = "AIzaSyA9PyXDHJQ8yrO-NCQV1e5sNJGPi0-x460"
    
    global chat_log, chat_list
    client = genai.Client(api_key=gemini_api_key)

    # 設定描述
    setting = [
            # "(用HTML格式回答)",
            # "你是一個AI聊天機器人/*繁體中文為主*/"
            # "以下是我們的談話內容(gemini: 你, user: 我)(不用輸出'gemini: ')",
            chat_log,
            ]
    
    string = request.POST.get("string")
    if string:
        chat1 = "\n".join(setting) + string
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=chat1,
            )        
        
        user = "user: " + string + "\n"
        responseText = response.text.replace('```html','').replace('```','')
        res = f"gemini: {responseText}"

        chat_list.append(('USER',string))
        chat_list.append(('AI', responseText.strip()))

        chat_log += (user + res)

    return render(request, "gemini_web.html", {"datas": chat_list})