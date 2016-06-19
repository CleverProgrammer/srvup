from django.db import models

# Create your models here.
from accounts.models import MyUser

from videos.models import Video


class CommentManager(models.Manager):
    def all(self):
        return super(CommentManager, self).filter(active=True).filter(parent=None)

    def create_comment(self, user=None, text=None, path=None, video=None):
        if not path:
            raise ValueError('Must include a path when adding a comment')

        if not user:
            raise ValueError('Must include a user when adding a comment')

        comment = self.model(user=user, path=path, text=text)

        if video:
            comment.video = video

        comment.save(using=self._db)
        return comment


class Comment(models.Model):
    # Make sure that they are a user
    user = models.ForeignKey(MyUser)
    parent = models.ForeignKey('self', null=True, blank=True)
    path = models.CharField(max_length=350)
    video = models.ForeignKey(Video, null=True, blank=True)
    text = models.TextField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    objects = CommentManager()

    class Meta:
        ordering = ('-timestamp',)

    def __str__(self):
        return self.text

    @property
    def is_child(self):
        if self.parent is not None:
            return True
        return False

    def get_children(self):
        if self.is_child:
            return None
        return Comment.objects.filter(parent=self)
