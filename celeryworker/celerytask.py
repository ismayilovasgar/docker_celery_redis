from celery import Celery

app = Celery("task")
app.config_from_object("celeryconfig")
app.conf.broker_connection_retry_on_startup = True


@app.task
def add_numbers():
    return "1---***"