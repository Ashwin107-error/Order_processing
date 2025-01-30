from celery import Celery
from flask_app.config import celery_app, db
from bson import ObjectId

@celery_app.task
def process_order(order_id):
    db.orders.update_one(
        {"_id": ObjectId(order_id)},
        {"$set": {"status": "Processed"}}
    )
