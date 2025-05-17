from django.db import models

# python manage.py makemigrations 資料表設定檔
# python manage.py migrate        同步到資料庫

class UserData(models.Model):
    GENDER_CHOICES = (
        (0, "男"),
        (1, "女")
    )
    name = models.CharField(max_length=10)
    phone = models.CharField(max_length=10)
    gender = models.IntegerField(choices=GENDER_CHOICES, default=0)
    age = models.IntegerField(max_length=200)
    create_at = models.DateTimeField(auto_now=True)

    class UserData:
        pass