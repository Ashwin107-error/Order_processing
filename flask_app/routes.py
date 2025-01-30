from flask import Blueprint, request, jsonify
from flask_app.db import db
from flask_app.tasks import process_order_task

order_blueprint = Blueprint("orders", __name__)

@order_blueprint.route("/", methods=["POST"])
def create_order():
    """Create a new order."""
    data = request.get_json()
    print(data,"HHHHHHHHH")

    if not data or "order_id" not in data or "items" not in data:
        return jsonify({"error": "Invalid request"}), 400

    # Store order in MongoDB
    db.orders.insert_one(data)

    # Send task to RabbitMQ
    # process_order_task.delay(data)

    return jsonify({"message": "Order placed successfully"}), 201
