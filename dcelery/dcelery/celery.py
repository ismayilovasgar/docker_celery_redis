import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dcelery.settings")

app = Celery("dcelery")
app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.broker_connection_retry_on_startup = True

# CELERY_BROKER_URL = "redis://redis:6379/0"
# CELERY_RESULT_BACKEND = "redis://redis:6379/0"


@app.task
def add_numbers():
    return "@app.task-1"

app.autodiscover_tasks()
