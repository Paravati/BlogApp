from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Roboczy'),
        ('published', 'Opublikowany')
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.CASCADE)
    body = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, defaul='draft')

    class Meta:
        """zawiera metadane; podczas wykonywania zapytania do bazy nakazujemy Django domyslne
        sortowanie wynikow w kolejnosci malejacej wzgledem kolumny publish (poprzez umieszczenie
        znaku minus przed publish)"""
        ordering = ('-publish', )

    def __str__(self):  # domyslna czytelna dla czlowieka reprezentacja obiekt
        return self.title
