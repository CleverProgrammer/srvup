from django.shortcuts import render
from .models import Video


# Create your views here.

def video_detail(request, id):
    context = {}
    context['object'] = Video.objects.get(id=id)
    return render(request, 'videos/video_detail.html', context)


def video_list(request):
    context = {}
    context['queryset'] = Video.objects.all()
    return render(request, 'videos/video_list.html', context)

# def video_edit(request):
#     context = {}
#     return render(request, 'videos/video_detail.html', context)
#
# def video_create(request):
#     context = {}
#     return render(request, 'videos/video_detail.html', context)
