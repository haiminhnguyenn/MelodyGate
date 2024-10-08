from flask import current_app as app
from app.extensions import db
from flask_login import UserMixin
from sqlalchemy import String, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from itsdangerous import URLSafeTimedSerializer as Serializer
from typing import Optional
from app.extensions import login_manager
from werkzeug.security import generate_password_hash, check_password_hash


class UserProfile(UserMixin, db.Model):
    __tablename__ = "user_profile"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(128), nullable=False)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    confirmed: Mapped[bool] = mapped_column(Boolean, default=False)
    role: Mapped[str] = mapped_column(String(15), default="user")
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
        db.session.add(self)
        db.session.commit()
        return True
    
    
    def generate_reset_token(self, expiration=3600):
        s = Serializer(app.config["SECRET_KEY"])
        return s.dumps(
            {"reset": self.id}, 
            salt="reset-salt", 
            max_age=expiration
        )
        
    
    def reset_password(self, new_password):
        self.password = new_password
        db.session.add(self)
        db.session.commit()
    
    
    @property
    def password(self):
        raise AttributeError("password is not a readable attribute")
    
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    
    
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    

login_manager.user_loader
def load_user(user_id):
    return db.session.get(UserProfile, int(user_id))