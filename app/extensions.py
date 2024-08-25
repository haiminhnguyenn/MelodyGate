from flask_sqlalchemy import SQLAlchemy
from app.models.base import Base
from flask_mail import Mail
from flask_login import LoginManager
from flask_cors import CORS

db = SQLAlchemy(model_class=Base)
mail = Mail()
login_manager = LoginManager()
cors = CORS()