from celery import shared_task

@shared_task
def task1_dcelery():
    return "task-1-dcelery"

@shared_task
def task2_dcelery():
    return "task-2-dcelery"