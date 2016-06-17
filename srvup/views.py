from django.shortcuts import render
from django.utils.safestring import mark_safe
from videos.models import Video


def home(request):
    name = 'Rafeh Qazi'
    videos = Video.objects.all()
    embeds = [(mark_safe(video.embed_code)) for video in videos]
    print(isinstance(embeds[0], str))
    context = {
        'name': name,
        'number': videos.count(),
        'videos': videos,
        'embeds': embeds,
    }
    return render(request, 'home.html', context)
