from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE


UserModel = get_user_model()


class Post(models.Model):
    TITLE_MAX_LEN = 200

    title = models.CharField(
        max_length=TITLE_MAX_LEN,
        unique=True,
    )

    author = models.ForeignKey(
        User,
        on_delete=CASCADE,
        related_name='blog_posts',
    )

    content = RichTextField()

    created_on = models.DateTimeField(
        auto_now_add=True,
    )

    updated_on = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class PostComment(models.Model):
    COMMENT_MAX_LEN = 300

    author = models.ForeignKey(
        UserModel,
        on_delete=CASCADE,
    )

    post = models.ForeignKey(
        Post,
        on_delete=CASCADE,
        related_name='comments'
    )

    body = models.TextField(
        max_length=COMMENT_MAX_LEN,
    )

    created_on = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f'Comment by {self.author}.'
