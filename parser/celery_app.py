from celery import Celery

app = Celery('celery_app', include=['tasks'])
app.config_from_object('celeryconfig')

app.conf.beat_schedule = {
    'get_new_data_every_hour': {
        'task': 'tasks.update_bd',
        'schedule': 600.0
    }
}

# celery -A celery_app beat --loglevel=INFO
# celery -A celery_app worker --loglevel=INFO -P eventlet
