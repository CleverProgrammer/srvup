from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
from django.utils.text import slugify

from .slugify_snippet import unique_slugify


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
    slug = models.SlugField(null=True, blank=True)
    active = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    free_preview = models.BooleanField(default=False)
    category = models.ForeignKey("Category")
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    objects = VideoManager()

    class Meta:
        unique_together = ('slug', 'category')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(viewname='video_detail',
                       kwargs={'vid_slug': self.slug, 'cat_slug': self.category.slug})

    def save(self, **kwargs):
        unique_slugify(self, self.title)
        super(Video, self).save(**kwargs)


# def video_post_save_receiver(sender, instance, created, *args, **kwargs):
#     print("Signal sent")
#     if created:
#         slug_title = slugify(instance.title)
#         new_slug = '{} {} {}'.format(instance.title, instance.category.slug, instance.id)
#         try:
#             obj_exists = Video.objects.get(slug=slug_title, category=instance.category)
#             instance.slug = slugify(new_slug)
#             instance.save()
#             print("Model exists, new slug generated")
#         except Video.DoesNotExist:
#             instance.slug = slug_title
#             instance.save()
#             print("New slug and model created")
#         except Video.MultipleObjectsReturned:
#             instance.slug = slugify(new_slug)
#             instance.save()
#             print('multiple models exists, new slug generated')
#         except:
#             pass


# post_save.connect(video_post_save_receiver, sender=Video)


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
