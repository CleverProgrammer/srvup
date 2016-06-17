from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
from videos.models import Video


@login_required
def home(request):
    print(request.user)
    print(request.user.is_authenticated())
    name = 'Rafeh Qazi'
    videos = Video.objects.all()
    embeds = [mark_safe(video.embed_code) for video in videos]
    context = {
        'name'  : name,
        'number': videos.count(),
        'videos': videos,
        'embeds': embeds,
    }
    return render(request, 'home.html', context)


def login(request):
    context = {

    }
    return render(request, 'login.html', context)