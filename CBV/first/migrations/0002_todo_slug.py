# Generated by Django 3.1.6 on 2021-02-15 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
