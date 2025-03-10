from dcelery.celery_config import app

@app.task(queue="task")
def my_task():
    pass