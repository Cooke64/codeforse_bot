import os

broker_url = 'redis://localhost:6379/0'
broker = broker_url if os.environ['DEBUG'] else os.environ['CELERY_BROKER_URL']
task_serializer = 'json'
result_serializer = 'json'
accept_content = ('json',)
timezone = 'Europe/Moscow'
enable_utc = True
