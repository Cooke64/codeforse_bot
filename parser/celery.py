from celery import Celery


# CELERY_BROKER_URL = 'redis://localhost:6379'
#
# app = Celery('parser', include=['parser.tasks'])

# app.conf.broker_url = CELERY_BROKER_URL
# app.conf.beat_schedule = {
#     'update_bd': {
#         'task': 'parser.tasks.update_bd',
#         'schedule': crontab(
#             minute=60,
#         ),
#     },
# }

@app.task
def func(a, b):
    return a + b

