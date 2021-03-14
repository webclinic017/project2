import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')

app = Celery('djangoProject')
app.config_from_object('django.conf:settings')

app.autodiscover_tasks()
app.conf.beat_schedule = {
    'send-report-every-morning': {
        'task': 'watchlists.tasks.send_watchlist_report',
        'schedule': crontab(),
    },
}
