from django.shortcuts import render

from .models import Announcement

# Create your views here.
def announcements(request):
    announcements = Announcement.objects.all()
    return render(request, 'announcements/announcements.html', {'announcements': announcements})
