from django import forms
from ..models.announcement import Announcement

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ["title", "content", "startTime", "endTime"]