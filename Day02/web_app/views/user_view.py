from django.shortcuts import render

from ..models.user_data import UserData

def register(request):
    data = {
        'gender_choices': UserData.GENDER_CHOICES
    }

    if request.method == 'POST':
        in_name = request.POST.get('name')
        in_phone = request.POST.get('phone')
        in_gender = request.POST.get('gender')
        in_age = request.POST.get('age')

        UserData.objects.create(
            name=in_name,
            phone=in_phone,
            gender=in_gender,
            age=in_age
        )

    data['msg'] = '新增成功'
    
    return render(request, "register.html", data)
