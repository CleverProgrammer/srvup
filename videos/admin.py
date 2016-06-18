from django.contrib import admin

# Register your models here.
from .models import Video, Category

# class VideoAdmin(admin.ModelAdmin):
    # exclude = []

admin.site.register(Video)
admin.site.register(Category)
