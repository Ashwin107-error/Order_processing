from celery import Celery
from flask_app.config import config

celery_app = Celery(
    "tasks",
    broker=config.CELERY_BROKER_URL,
    backend=config.CELERY_RESULT_BACKEND,
)
