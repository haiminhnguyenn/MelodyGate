from flask_sqlalchemy import SQLAlchemy
from app.models.base import Base
from flask_mail import Mail

db = SQLAlchemy(model_class=Base)
mail = Mail()