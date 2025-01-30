from flask_app.celery_worker import celery_app

@celery_app.task
def process_order_task(order_data):
    """Background task for order processing."""
    print(f"Processing order: {order_data['order_id']}")
    return {"status": "Processed", "order_id": order_data["order_id"]}
