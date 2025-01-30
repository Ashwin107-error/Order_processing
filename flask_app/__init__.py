from flask import Flask
from flask_app.routes import order_blueprint
from flask_app.db import init_db

def create_app():
    app = Flask(__name__)
    
    # Initialize MongoDB
    init_db()

    # Register Blueprints (Modular API)
    app.register_blueprint(order_blueprint, url_prefix="/api/orders")

    return app
