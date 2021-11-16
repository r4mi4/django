from django.db import models


class Number(models.Model):
    task_id = models.CharField(max_length=100)
    x = models.IntegerField()
    y = models.IntegerField()
    result = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.x} + {self.y} = {self.result}'
