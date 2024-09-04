from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_mail import Mail
from flask_login import LoginManager
from flask_cors import CORS


class Base(DeclarativeBase):
  pass


db = SQLAlchemy(model_class=Base)
login_manager = LoginManager()
mail = Mail()
cors = CORS()