from sqlalchemy import select
from src.exception.resource_not_found_exception import ResourceNotFoundException
from src.model.movie import Movie

class MovieDAO:
    def __init__(self, session):
        self.session = session

    def create_movie(self, m: Movie):
        try:
            self.session.add(m)
            self.session.flush()
            self.session.commit()
            return m
        except Exception:
            self.session.rollback()
            raise

    def fetch_movies(self):
        statement = select(Movie)
        return self.session.execute(statement).scalars().all()

    def fetch_movie_by_id(self, mid: int):
        movie = self.session.get(Movie, mid)
        if not movie:
            raise ResourceNotFoundException("Movie not found")
        return movie

    def update_movie(self, mid: int, m: Movie):
        db_movie = self.session.get(Movie, mid)
        if not db_movie:
            raise ResourceNotFoundException("Movie not found")
        try:
            db_movie.title = m.title
            db_movie.genre = m.genre
            db_movie.year = m.year
            self.session.flush()
            self.session.commit()
            return db_movie
        except Exception :
            self.session.rollback()
            raise

    def delete_movie(self, mid: int):
        db_movie = self.session.get(Movie, mid)
        if not db_movie:
            raise ResourceNotFoundException("Movie not found")
        try:
            self.session.delete(db_movie)
            self.session.commit()
            return db_movie
        except Exception:
            self.session.rollback()
            raise
