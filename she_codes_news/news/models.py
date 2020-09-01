from django.db import models
from django.contrib.auth import get_user_model


class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    # author = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="stories",
    )
    pub_date = models.DateTimeField()
    content = models.TextField()
    image_source = models.CharField(max_length=200, default="https://picsum.photos/600")
