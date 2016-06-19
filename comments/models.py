from django.db import models

# Create your models here.
from accounts.models import MyUser

from videos.models import Video


class CommentManager(models.Manager):
    def create_comment(self, user=None, comment=None, path=None, video=None):
        if not path:
            raise ValueError('Must include a path when adding a comment')

        if not user:
            raise ValueError('Must include a user when adding a comment')

        comment = self.model(user=user, path=path, comment=comment)

        if video:
            comment.video = video

        comment.save(using=self._db)
        return comment


class Comment(models.Model):
    # Make sure that they are a user
    user = models.ForeignKey(MyUser)
    path = models.CharField(max_length=350)
    video = models.ForeignKey(Video, null=True, blank=True)
    text = models.TextField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    objects = CommentManager()

    def __str__(self):
        return self.user.username
