from celery import shared_task
import time

# @shared_task
# def task1_dcelery():
#     return "task-1-dcelery"

# @shared_task
# def task2_dcelery():
#     return "task-2-dcelery"


# @shared_task
# def tp1():
#     time.sleep(3)
#     return

# @shared_task
# def tp2():
#     time.sleep(3)
#     return

# @shared_task
# def tp3():
#     time.sleep(3)
#     return

# @shared_task
# def tp4():
#     time.sleep(3)
#     return


# ! way -1
@shared_task(rate_limit="10/m")
def tp1(queue="celery"):
    time.sleep(5)
    return "tp1"


@shared_task
def tp2(queue="celery_1"):
    time.sleep(5)
    return "tp2"


@shared_task
def tp3(queue="celery_2"):
    time.sleep(5)
    return "tp3"


@shared_task
def tp4(queue="celery_3"):
    time.sleep(5)
    return "tp4"
