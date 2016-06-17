from django.contrib import admin

# Register your models here.
from .models import Video

# class VideoAdmin(admin.ModelAdmin):
    # exclude = []

admin.site.register(Video)
