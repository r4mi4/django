from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, null=True)


class Comment(models.Model):
    todo = models.ForeignKey(Todo, models.CASCADE, related_name='tcomment')
    name = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.name
