from flask import Flask
from config import Config
from app.extensions import db

def create_app(class_config=Config):
    app = Flask(__name__)
    app.config.from_object(class_config)
    
    db.init_app(app)
    
    return app