from django.contrib import admin

# Register your models here.
from .models import Video, Category


class VideoAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']
    # fields = ['title', 'embed_code']
    exclude = ('slug',)

    class Meta:
        model = Video


admin.site.register(Video, VideoAdmin)
admin.site.register(Category)
