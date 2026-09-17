
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.db_config import Base
class Movie(Base):
    __tablename__ = 'movie'
    id:Mapped[int]=mapped_column(Integer,primary_key=True)
    title:Mapped[str]=mapped_column(String(100),nullable=False)
    genre:Mapped[str]=mapped_column(String(100),nullable=False)
    year:Mapped[int]=mapped_column(Integer,nullable=False)

    reviews=relationship("Review",back_populates="movie",cascade="all,delete-orphan")

