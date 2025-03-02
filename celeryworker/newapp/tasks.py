from celery import shared_task

@shared_task
def task1_celeryworker():
    return "task-1-celeryworker"

@shared_task
def task2_celeryworker():
    return "task-2-celeryworker"