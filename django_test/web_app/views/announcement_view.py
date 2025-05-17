from django.shortcuts import render, get_object_or_404, redirect
from ..forms.announcement_form import AnnouncementForm
from ..models.announcement import Announcement

def announcementCreate(request):
    form = AnnouncementForm()

    if request.method == "POST":
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('announcementList')
        
    return render(request, "announcement/create.html", {"form": form})

def announcementUpdate(request, id):
    announcement = get_object_or_404(Announcement, pk = id)
    form = AnnouncementForm(instance = announcement)
    data = {}
    if request.method == "POST":
        form = AnnouncementForm(request.POST, instance = announcement)
        if form.is_valid():
            form.save()
            data['msg'] = "更改成功"
            return redirect('announcementList')
    data["form"] = form
    return render(request, "announcement/update.html", data)

def announcementList(request):
    announcements = Announcement.objects.all()
    return render(request, "announcement/admin.html", {"announcements": announcements})

def announcementDelete(_, id):
    announcement = get_object_or_404(Announcement, pk=id)
    announcement.delete()
    return redirect('announcementList')

