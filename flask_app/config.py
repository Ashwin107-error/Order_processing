import os

class Config:
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/orders_db")
    CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", "pyamqp://guest@localhost//")
    CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND", "rpc://")

config = Config()
