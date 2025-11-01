from flask import Flask
from .routes import register_routes

def create_app():
    app = Flask(__name__)
    # basic configuration
    app.config.from_object("config")
    # register routes
    register_routes(app)
    return app