from django.shortcuts import render

from videos.models import Video


def home(request):
    name = 'Rafeh Qazi'
    videos = Video.objects.all()
    context = {
        'name': name,
        'number': videos.count(),
        'videos': videos,
    }
    return render(request, 'home.html', context)
