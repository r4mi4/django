import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CeleyInDjango.settings')
celery_app = Celery('CeleyInDjango')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks(settings.INSTALLED_APPS)