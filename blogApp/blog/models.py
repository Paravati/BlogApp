from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Roboczy'),
        ('published', 'Opublikowany'),
    )
    objects = models.Manager()  # manager domyslny
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    published = PublishedManager()   # manager niestandardowy   -> to było wcześniej
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        """zawiera metadane; podczas wykonywania zapytania do bazy nakazujemy Django domyslne
        sortowanie wynikow w kolejnosci malejacej wzgledem kolumny publish (poprzez umieszczenie
        znaku minus przed publish)"""
        ordering = ('-published', )

    def __str__(self):  # domyslna czytelna dla czlowieka reprezentacja obiekt
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                        args=[self.publish.year, self.publish.strftime('%m'),
                              self.publish.strftime('%d'), self.slug])
