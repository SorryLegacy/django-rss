from django.db import models


class Url(models.Model):
    url = models.URLField(verbose_name="link")
    limit = models.IntegerField(verbose_name="Limit", null=True, blank=True)

    def __str__(self):
        return self.url


class PostFromUrl(models.Model):
    title = models.CharField(verbose_name="News", max_length=300)
    date = models.DateTimeField('date published', auto_now=False)
    link = models.URLField(verbose_name="link", max_length=300)
    img = models.URLField(verbose_name="image", null=True, blank=True, max_length=300)

    def __str__(self):
        return self.title
