from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe

from accounts.forms import RegisterForm
from accounts.models import MyUser

from videos.models import Video

from .forms import LoginForm


def home(request):
    # print(request.user)
    # print(request.user.is_authenticated())
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password2']
        # MyUser.objects.create(username=username, email=email, password=password)
        # print(username, email, password)
        new_user = MyUser()
        new_user.username = username
        new_user.email = email
        new_user.set_password(password)
        new_user.save()
        # Add message for success
        return redirect('login')
        # return HttpResponseRedirect(reverse('login'))
        # email user
        # create user profile instance


    # name = 'Rafeh Qazi'
    # videos = Video.objects.get_featured()
    # embeds = [mark_safe(video.embed_code) for video in videos]
    context = {
        'form': form,
        'action_value': '/',
        'submit_btn_value': 'Register',
        #     'name'  : name,
        #     'number': videos.count(),
        #     'videos': videos,
        #     'embeds': embeds,
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
            return redirect('home')
    context = {'form': form}
    return render(request, 'login.html', context)


def auth_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
