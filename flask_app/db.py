from pymongo import MongoClient
from flask_app.config import config

client = MongoClient(config.MONGO_URI)
db = client["orders_db"]

def init_db():
    """Ensure indexes and initial setup for MongoDB."""
    db.orders.create_index("order_id", unique=True)
