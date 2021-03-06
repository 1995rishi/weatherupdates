BROKER_URL ='mongodb://localhost:27017/'
from datetime import *
from celery.schedules import crontab

CELERY_RESULT_BACKEND = "mongodb"
CELERY_MONGODB_BACKEND_SETTINGS = {
    "host": "127.0.0.1",
    "port": 27017,
    "database": "weather", 
    "taskmeta_collection": "stock_taskmeta_collection",
}

CELERY_TIMEZONE = "Asia/Kolkata"
CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds': {
        'task': 'tasks.add',
        'schedule': timedelta(seconds=3)
    },
}
