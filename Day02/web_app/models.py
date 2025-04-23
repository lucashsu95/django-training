from django.db import models

# python manage.py makemigrations web_app 資料表設定檔
# python manage.py migrate 同步到資料庫

class UserData(models.Model):
    GENDER_CHOICES = (
        (0, "公"),
        (1, "母"),
    )
    
    name = models.CharField(max_length=10)
    phone = models.CharField(max_length=11)
    gender = models.IntegerField(choices=GENDER_CHOICES, default=0)
    age = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
