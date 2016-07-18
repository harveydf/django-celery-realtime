import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_realtime.settings')

from django.conf import settings  # noqa

app = Celery('celery_realtime')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.conf.update(
    BROKER_URL = 'redis://redis:6379/0',
    CELERY_RESULT_BACKEND = 'redis://redis:6379/0',
)
