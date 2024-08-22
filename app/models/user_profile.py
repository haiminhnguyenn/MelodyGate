from app.extensions import db
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional


class UserProfile(db.Model):
    id: Mapped[str] = mapped_column(String(50), primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(100), nullable=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    gender: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    birthday: Mapped[Optional[str]] = mapped_column(String(15), nullable=True)
    location: Mapped[Optional[str]] = mapped_column(String(250), nullable=True)