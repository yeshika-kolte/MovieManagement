from sqlalchemy import Integer, String, ForeignKey, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.db_config import Base

class Review(Base):
    __tablename__ = 'review'
    id:Mapped[int]=mapped_column(Integer,primary_key=True)
    user_id:Mapped[int]=mapped_column(Integer,ForeignKey('user.id'))
    movie_id:Mapped[int]=mapped_column(Integer,ForeignKey('movie.id'))
    rating:Mapped[float]=mapped_column(Float,nullable=False)
    comment:Mapped[str]=mapped_column(String(255),nullable=False)

    user = relationship("User",back_populates="reviews")
    movie = relationship("Movie",back_populates="reviews")