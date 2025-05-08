from django.shortcuts import render, get_object_or_404

from web_app.models.announcement import Announcement
from ..forms.announcement_form import AnnouncementForm

def announcement_create(request):
    form = AnnouncementForm()
    data = {}
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            form.save()
            data['msg'] = '新增成功'
    data['form'] = form
    print(data)
    return render(request, "announcement/create.html", data)

    
def announcement_update(request, id):
    announcement = get_object_or_404(Announcement, pk=id)
    form = AnnouncementForm(instance=announcement)
    data = {}
    if request.method == 'POST':
        form = AnnouncementForm(request.POST, instance=announcement)
        if form.is_valid():
            form.save()
            data['msg'] = '更改成功'
    data['form'] = form
    return render(request, 'announcement/update.html', data)