from django.shortcuts import render


def home(request):
    name = 'Rafeh Qazi'
    context = {
    'name': name,
        }
    return render(request, 'home.html', context)
