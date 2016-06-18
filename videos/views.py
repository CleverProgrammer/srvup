from django.shortcuts import render, Http404
from django.contrib.auth.decorators import login_required

from .models import Video, Category


# Create your views here.

@login_required
def video_detail(request, cat_slug, vid_slug):
    try:
        cat = Category.objects.get(slug=cat_slug)
    except:
        raise Http404
    try:
        context = {}
        context['object'] = Video.objects.get(slug=vid_slug)
        return render(request, 'videos/video_detail.html', context)
    except:
        raise Http404


def category_list(request):
    context = {}
    context['queryset'] = Category.objects.all()
    return render(request, 'videos/category_list.html', context)


@login_required
def category_detail(request, cat_slug):
    try:
        context = {}
        cat = Category.objects.get(slug=cat_slug)
        context['object'] = cat
        context['queryset'] = cat.video_set.all()
        return render(request, 'videos/video_list.html', context)
    except:
        raise Http404

# def video_edit(request):
#     context = {}
#     return render(request, 'videos/video_detail.html', context)
#
# def video_create(request):
#     context = {}
#     return render(request, 'videos/video_detail.html', context)
