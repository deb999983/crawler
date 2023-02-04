import os
from celery import Celery

os.environ["DJANGO_SETTINGS_MODULE"] = "settings"

app = Celery(
    'worker',
    broker='redis://crawler_queue:6379/0',
    backend='db+postgresql://postgres:postgres@web_server_db/celery',
    include=['tasks']
)