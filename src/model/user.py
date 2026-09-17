from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.db_config import Base


class User(Base):
    __tablename__ = 'user'
    id:Mapped[int]=mapped_column(Integer,primary_key=True)
    username:Mapped[str]=mapped_column(String(100),nullable=False)
    password:Mapped[str]=mapped_column(String(100),nullable=False)
    email:Mapped[str]=mapped_column(String(100),nullable=False)
    full_name:Mapped[str]=mapped_column(String(100),nullable=False)
    role:Mapped[str]=mapped_column(String(100),nullable=False)
    reviews = relationship("Review", back_populates="user", cascade="all,delete-orphan")
