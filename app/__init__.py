from flask import Flask
from config import Config
from app.extensions import db, mail
from celery import Celery

celery = Celery(__name__, broker=Config.CELERY_BROKER_URL)

def create_app(class_config=Config):
    app = Flask(__name__)
    app.config.from_object(class_config)
    
    db.init_app(app)
    mail.init_app(app)
    
    celery.conf.update(app.config)
    
    return app