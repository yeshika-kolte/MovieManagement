from src.dao.movie_dao import MovieDAO
from src.model.movie import Movie

class MovieService:
    def __init__(self, session):
        self.movie_dao = MovieDAO(session)

    def add_movie(self, title, genre, year):
        movie = Movie(title=title, genre=genre, year=year)
        return self.movie_dao.create_movie(movie)

    def list_movies(self):
        return self.movie_dao.fetch_movies()

    def find_movie(self, movie_id: int):
        return self.movie_dao.fetch_movie_by_id(movie_id)

    def update_movie(self, movie_id: int, title, genre, year):
        movie = Movie(title=title, genre=genre, year=year)
        return self.movie_dao.update_movie(movie_id, movie)

    def delete_movie(self, movie_id: int):
        return self.movie_dao.delete_movie(movie_id)
