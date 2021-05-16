from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth import get_user_model


class LinkPost(models.Model):
    author = models.ForeignKey(
        get_user_model(),
        related_name='links',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=300)
    link = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    liked_by = models.ManyToManyField(get_user_model(), related_name='likes')
    total_likes = models.PositiveIntegerField(
        default=0, validators=[MinValueValidator(0)]
    )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.title}'
