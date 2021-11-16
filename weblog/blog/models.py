from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class PublishModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='publish')


class Article(models.Model):
    STATUS = (
        ('draft', 'Draft'),
        ('publish', 'Publish'),
    )
    title = models.CharField(max_length=120, default='title')
    # todo : prepopulated_fields = {'slug': ('title',)} --> need allow_unicode for support persian in slug auto !
    # slug = models.SlugField(max_length=120, unique=True, default='slug', allow_unicode='true')
    slug = models.SlugField(max_length=120, unique=True, default='slug')
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextUploadingField()
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS, max_length=20, default='Draft')
    objects = models.Manager()
    publish = PublishModelManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:article_detail', args=[self.id, self.slug])
