from django.db import models

# python manage.py makemigrations 資料表設定檔
# python manage.py migrate        同步到資料庫

class Announcement(models.Model):
    title = models.CharField(max_length=25, blank=False)
    content = models.CharField(max_length=200, blank=False)
    startTime = models.DateTimeField(null=True, blank=True)
    endTime = models.DateTimeField(null=True, blank=True)
    createTime = models.DateTimeField(auto_now=True)