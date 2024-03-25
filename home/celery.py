import os
from celery import Celery

# settings up the default django settings file
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "home.settings")

# creating celery object with a name home
celery = Celery("home")

# configuring all celery setting in settings.py file
celery.config_from_object("django.conf:settings", namespace="CELERY")

# allow to discover all task accross differen project
celery.autodiscover_tasks()
