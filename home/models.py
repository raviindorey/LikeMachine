from django.db import models
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

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.title}'
