"""srvup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from srvup import views as srvup_views
from accounts import views as account_views
from videos import views as video_views

urlpatterns = [
    # url(r'^$', TemplateView.as_view(template_name='base.html'), name='home'),
    url(r'^staff/$', srvup_views.staff_home, name='staff'),
    url(r'^courses/$', video_views.category_list, name='category_list'),
    url(r'^courses/(?P<cat_slug>[\w-]+)/$', video_views.category_detail, name='category_detail'),
    url(r'^courses/(?P<cat_slug>[\w-]+)/(?P<vid_slug>[\w-]+)/$', video_views.video_detail, name='video_detail'),
    url(r'^$', srvup_views.home, name='home'),
    url(r'^admin/', admin.site.urls),
]

# Auth login/logout

urlpatterns += [
    url(r'^login/$', account_views.auth_login, name='login'),
    url(r'^logout/$', account_views.auth_logout, name='logout'),
]
