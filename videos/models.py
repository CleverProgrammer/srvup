from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.
class VideoQuerySet(models.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True)


class VideoManager(models.Manager):
    def get_queryset(self):
        return VideoQuerySet(self.model, using=self._db)

    def get_featured(self):
        return self.get_queryset().active().featured()
        # return super(VideoManager, self).filter(featured=True)

    def all(self):
        return self.get_queryset().active()


class Video(models.Model):
    title = models.CharField(max_length=120)
    embed_code = models.CharField(max_length=500, blank=True, null=True)
    active = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    free_preview = models.BooleanField(default=False)

    objects = VideoManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(viewname='video_detail', kwargs={'id': self.id})
