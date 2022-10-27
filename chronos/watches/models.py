from datetime import date

from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import CASCADE

from chronos.watches.validators import file_size


class Watch(models.Model):
    BRAND_MAX_LEN = 30

    MODEL_MAX_LEN = 30

    REFERENCE_NUMBER_MAX_LEN = 30

    YEAR_MIN_VALUE = 1800
    YEAR_MAX_VALUE = date.today().year

    WATCH_STYLES_CHOICES = [
        ('Pocket', 'Pocket'),
        ('Railroad', 'Railroad'),
        ('Dress', 'Dress'),
        ('Field', 'Field'),
        ('Aviator', 'Aviator'),
        ('Dive', 'Dive'),
        ('Racing', 'Racing'),
        ('Digital', 'Digital'),
        ('Smart ', 'Smart'),
        ('Fashion', 'Fashion'),
    ]

    STYLE_MAX_LEN = max([len(style[1]) for style in WATCH_STYLES_CHOICES])

    CONDITION_MAX_LEN = 100

    PRICE_MIN_VALUE = 0

    DESCRIPTION_MAX_LEN = 500

    owner = models.ForeignKey(
        User,
        on_delete=CASCADE
    )

    brand = models.CharField(
        max_length=BRAND_MAX_LEN,
    )

    model = models.CharField(
        max_length=MODEL_MAX_LEN,
    )

    reference_number = models.CharField(
        blank=True,
        null=True,
        max_length=REFERENCE_NUMBER_MAX_LEN,
    )

    year = models.IntegerField(
        blank=True,
        null=True,
        validators=[
            MinValueValidator(YEAR_MIN_VALUE),
            MaxValueValidator(YEAR_MAX_VALUE)],
    )

    style = models.CharField(
        max_length=STYLE_MAX_LEN,
        choices=WATCH_STYLES_CHOICES,
    )

    condition = models.TextField(
        null=True,
        blank=True,
        max_length=CONDITION_MAX_LEN,
    )

    price_paid = models.FloatField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(PRICE_MIN_VALUE)
        ]
    )

    description = models.TextField(
        null=True,
        blank=True,
        max_length=DESCRIPTION_MAX_LEN,
    )

    image = models.ImageField(
        null=True,
        blank=True,
        upload_to='watches',
        validators=(
            file_size,
        )
    )

    likes = models.ManyToManyField(
        User,
        related_name='watch_likes'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name_plural = "watches"

    def like_count(self):
        return self.likes.count()

    def __str__(self):
        return f'{self.brand} {self.model}'


class WatchComment(models.Model):
    COMMENT_MAX_LEN = 300

    author = models.ForeignKey(
        User,
        on_delete=CASCADE,
    )
    watch = models.ForeignKey(
        Watch,
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