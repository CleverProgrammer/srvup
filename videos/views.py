from django.shortcuts import render, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from comments.models import Comment
from comments.forms import CommentForm

from .models import Video, Category


# Create your views here.

@login_required
def video_detail(request, cat_slug, vid_slug):
    path = request.get_full_path()

    try:
        cat = Category.objects.get(slug=cat_slug)
    except:
        raise Http404
    try:
        context = {}
        video = Video.objects.get(slug=vid_slug)
        context['object'] = video
        context['comments'] = video.comment_set.all()
        comment_form = CommentForm(request.POST or None)
        print(request.POST)
        if comment_form.is_valid():
            comment_text = comment_form.cleaned_data['text']
            new_comment = Comment.objects.create_comment(
                user=request.user,
                path=request.get_full_path(),
                text=comment_text,
                video=video)
            # TODO: Add comment thread and show that thread with a message
            return HttpResponseRedirect(video.get_absolute_url())
        context['comment_form'] = comment_form
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
