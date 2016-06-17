from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=120)
    embed_code = models.CharField(max_length=500, blank=True, null=True)
    active = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    free_preview = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(viewname='video_detail', kwargs={'id': self.id})
