from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.utils.safestring import mark_safe

from .forms import LoginForm

# Create your views here.


def auth_login(request):
    form = LoginForm(request.POST or None)
    next_url = request.GET.get('next')
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect(next_url)
    context = {'form': form}
    return render(request, 'login.html', context)


def auth_logout(request):
    logout(request)
    next_url = request.GET.get('next')
    return redirect(next_url)
