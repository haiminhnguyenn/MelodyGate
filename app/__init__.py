from flask import Flask
from config import Config
from app.extensions import db, mail, login_manager, cors
from celery import Celery

celery = Celery(__name__, broker=Config.CELERY_BROKER_URL)

def create_app(class_config=Config):
    app = Flask(__name__)
    app.config.from_object(class_config)
    
    db.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)
    cors.init_app(app, resources={
        r"/*": {
            "origins": "http://localhost:3000",
            "methods": ["GET", "POST", "PUT", "DELETE"]
        }
    })
    
    celery.conf.update(app.config)
    
    from app.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix="/auth")
    
    return app