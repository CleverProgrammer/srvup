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
    category = models.ForeignKey("Category")
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    objects = VideoManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(viewname='video_detail', kwargs={'id': self.id, 'cat_slug': self.category.slug})


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    title = models.CharField(max_length=120)
    description = models.TextField(max_length=5000, blank=True, null=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    slug = models.SlugField(unique=True)
    active = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(viewname='category_detail', kwargs={'cat_slug': self.category.slug})
