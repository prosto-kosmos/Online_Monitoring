import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'grath.settings')

app = Celery('grath')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


def get_inspect():
    return app.control.inspect()


def revoke_task(task_id):
    app.control.revoke(task_id)
