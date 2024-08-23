import os

class Config:
    SECRET_KEY = "MD-NM-HM"
    SQLALCHEMY_DATABASE_URI = "postgresql://haiminh:26032003@localhost:5432/melody_gate_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CELERY_BROKER_URL = "amqp://localhost"
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = "melodygate@gmail.com"
    MAIL_SUBJECT_PREFIX = "[Melody Gate]"