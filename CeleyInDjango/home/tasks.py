from celery import shared_task
import time
from django.core.mail import send_mail
from home.models import Number


@shared_task
def adding(x, y, id):
    time.sleep(10)
    num = Number.objects.get(id=id)
    num.result = x + y
    num.save()
    return num.result


@shared_task
def send_email():
    send_mail('Celery', 'this message for learning celery beat :) ', 'ramin@gmail.com',
              ['ramin@gmail.com'])
