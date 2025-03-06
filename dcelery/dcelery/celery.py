import os
from celery import Celery
from kombu import Queue

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dcelery.settings")
app = Celery("dcelery")
app.config_from_object("django.conf:settings", namespace="CELERY")

# CELERY_BROKER_URL = "redis://redis:6379/0"
# CELERY_RESULT_BACKEND = "redis://redis:6379/0"

# @app.task
# def add_numbers():
#     return "@app.task-1"

# ! priority - 1
# app.conf.broker_connection_retry_on_startup = True
# app.conf.task_routes = {
#     "newapp.tasks.task1": {"queue": "queue1"},
#     "newapp.tasks.task2": {"queue": "queue2"},
# }


# ! priority - 2
app.conf.task_default_rate_limit = "1/m"

app.conf.broker_transport_options = {
    "priority_steps": list(range(10)),
    "sep": "_",
    "queue_order_strategy": "priority",
}

app.conf.task_queues = (
    Queue("celery"),
    Queue("celery_1"),
    Queue("celery_2"),
    Queue("celery_3"),
)
# app.conf.task_default_queue = 'celery'

# app.conf.task_routes = {
#     'newapp.tasks.tp1': {'queue': 'celery'},
#     'newapp.tasks.tp2': {'queue': 'celery_1'},
#     'newapp.tasks.tp3': {'queue': 'celery_2'},
#     'newapp.tasks.tp4': {'queue': 'celery_3'},
# }


app.autodiscover_tasks()
