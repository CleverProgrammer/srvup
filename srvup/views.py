from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe

from .forms import LoginForm
from videos.models import Video


@login_required
def home(request):
    # print(request.user)
    # print(request.user.is_authenticated())
    name = 'Rafeh Qazi'
    videos = Video.objects.get_featured()
    embeds = [mark_safe(video.embed_code) for video in videos]
    context = {
        'name'  : name,
        'number': videos.count(),
        'videos': videos,
        'embeds': embeds,
    }
    return render(request, 'home.html', context)

@login_required(login_url='/staff/login/')
def staff_home(request):
    context = {}
    return render(request, 'home.html', context)

def auth_login(request):
    form = LoginForm(request.POST or None)
    next_url = request.GET.get('next')
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        # print(username, password)
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(next_url)
    context = {'form': form}
    return render(request, 'login.html', context)


def auth_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
