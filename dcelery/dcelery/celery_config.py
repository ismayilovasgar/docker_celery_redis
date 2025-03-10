import os, time
from celery import Celery
from kombu import Queue, Exchange

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dcelery.settings")
app = Celery("dcelery")
app.config_from_object("django.conf:settings", namespace="CELERY")

# ! priority - 2
# app.conf.task_default_rate_limit = "1/m"

# app.conf.broker_transport_options = {
#     "priority_steps": list(range(10)),
#     "sep": "_",
#     "queue_order_strategy": "priority",
# }

# app.conf.task_queues = (
#     Queue("celery"),
#     Queue("celery_1"),
#     Queue("celery_2"),
#     Queue("celery_3"),
# )

## ----------------------------------
app.conf.task_queues = [
    Queue(
        "tasks",
        Exchange("tasks"),
        routing_key="tasks",
        queue_arguments={"x-max-priority": 10},
    )
]

app.conf.task_acks_late = True
app.conf.task_default_priority = 5
app.conf.worker_prefetch_multiplier = 1
app.conf.worker_concurrency = 1


# @app.task(queue="tasks")
# def t1(a, b, message=None):
#     result = a + b
#     if message:
#         result = f"{message}:{result}"
#     return result

# @app.task(queue="tasks")
# def t2():
#     time.sleep(3)
#     return "t2"


# @app.task(queue="tasks")
# def t3():
#     time.sleep(3)
#     return "t3"

# def test():
#     result = t1.apply_async(args=[5,10],kwargs = {"message":"The sum is"})

#     # check if the task has completed
#     if result.ready():
#         print("Task has completed")
#     else:
#         print("Task is still running")

#     # check if the task completed successfully
#     if result.successfully():
#         print("Task completed Successfully")
#     else:
#         print("Task encountered an error")

#     # get the result of the task
#     try:
#         task_result = result.get()
#     except Exception as e:
#         print("An exception occurred", str(e))

#     # get the exception (if any) that occurred during task execution
#     exception = result.get(propagate=False)
#     if exception:
#         print("An exception occurred during task execution",str(exception))


# # Aynchronous task execution
# def execute_async():
#     result = t1.apply_async(args=[5,10],kwargs={"message":"The sum is"})
#     print("Task is running asynchronously")
#     print("Task ID:",result.task_id)


base_dir = os.getcwd()
task_folder = os.path.join(base_dir, "dcelery", "celery_tasks")

if os.path.exists(task_folder) and os.path.isdir(task_folder):
    task_modules = []
    for filename in os.listdir(task_folder):
        if filename.startswith("ex") and filename.endswith(".py"):
            module_name = f"dcelery.celery_tasks.{filename[:-3]}"

            module = __import__(module_name, fromlist=["*"])

            for name in dir(module):
                obj = getattr(module, name)
                # if callable(obj) and name.startswith("my_task"):
                if callable(obj):
                    task_modules.append(f"{module_name}.{name}")

    app.autodiscover_tasks(task_modules)
## ----------------------------------


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

# app.conf.task_default_queue = 'celery'
# app.conf.task_routes = {
#     'newapp.tasks.tp1': {'queue': 'celery'},
#     'newapp.tasks.tp2': {'queue': 'celery_1'},
#     'newapp.tasks.tp3': {'queue': 'celery_2'},
#     'newapp.tasks.tp4': {'queue': 'celery_3'},
# }


# app.autodiscover_tasks()
