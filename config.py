class Config:
    SECRET_KEY = "MD-NM-HM"
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:26032003@localhost:5432/melody_gate_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CELERY_BROKER_URL = "amqp://localhost"
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = "themelodygate@gmail.com"
    MAIL_PASSWORD = "Themelodygate66"
    MAIL_DEFAULT_SENDER = "themelodygate@gmail.com"
    MAIL_SUBJECT_PREFIX = "[Melody Gate]"