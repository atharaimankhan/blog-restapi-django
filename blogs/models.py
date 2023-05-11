from django.conf import settings
from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'Tag[id: {self.id}, name: {self.name}]'


class Blog(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="blogs",
        null=True,
        on_delete=models.SET_NULL,
    )
    published_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name="blogs", blank=True)

    class Meta:
        ordering = ("-published_at",)

    def __str__(self):
        return f"{self.title} by {self.author}"
