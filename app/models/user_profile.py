from flask import current_app as app
from app.extensions import db
from flask_login import UserMixin
from sqlalchemy import String, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from itsdangerous import URLSafeTimedSerializer as Serializer
from typing import Optional
from app.extensions import login_manager


class UserProfile(UserMixin, db.Model):
    __tablename__ = "user_profile"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(100), nullable=False)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    confirmed: Mapped[bool] = mapped_column(Boolean, default=False)
    name: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    bio: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)
    gender: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    birthday: Mapped[Optional[str]] = mapped_column(String(15), nullable=True)
    location: Mapped[Optional[str]] = mapped_column(String(250), nullable=True)
    
    
    def has_existed_email(self):
        user = db.session.execute(
            db.select(UserProfile)
            .where(UserProfile.email == self.email)
        ).scalar()
        if user:
            return True
        
        return False
    
    
    def has_existed_username(self):
        user = db.session.execute(
            db.select(UserProfile)
            .where(UserProfile.username == self.username)
        ).scalar()
        if user:
            return True
        
        return False
    
    
    def generate_confirmation_token(self, expiration=3600):
        s = Serializer(app.config["SECRET_KEY"])
        return s.dumps(
            {"confirm": self.id}, 
            salt="confirm-salt", 
            max_age=expiration
        )
    
    
    def confirm(self, token):
        s = Serializer(app.config["SECRET_KEY"])
        try:
            data = s.loads(token)
        except:
            return False
        
        if data.get("confirm") != self.id:
            return False
        
        self.confirmed = True
        db.session.commit()
        return True
    

login_manager.user_loader
def load_user(user_id):
    return db.session.get(UserProfile, int(user_id))