from flask import Flask, request, jsonify
from celery_tasks.tasks import process_order
from flask_app.config import db

app = Flask(__name__)

@app.route('/order', methods=['POST'])
def create_order():
    data = request.json
    new_order = {
        "item": data['item'],
        "quantity": data['quantity'],
        "status": "Pending"
    }
    order_id = db.orders.insert_one(new_order).inserted_id
    print(order_id,"JJJJJJ")

    # Send order to Celery for background processing
    process_order.apply_async(args=[str(order_id)])

    return jsonify({"message": "Order placed!", "order_id": str(order_id)})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
