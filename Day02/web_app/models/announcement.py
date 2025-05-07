from django.db import models

class Announcement(models.Model):
    title = models.CharField(max_length=25, blank=False)
    content = models.CharField(max_length=200, blank=False)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)