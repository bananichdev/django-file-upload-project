import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "file_upload_project.settings")
app = Celery("file_upload_project")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
