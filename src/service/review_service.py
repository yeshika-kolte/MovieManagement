from src.dao.review_dao import ReviewDAO
from src.model.review import Review

class ReviewService:
    def __init__(self, session):
        self.review_dao = ReviewDAO(session)

    def add_review(self, user_id, movie_id, rating, comment):
        review = Review(user_id=user_id, movie_id=movie_id, rating=rating, comment=comment)
        return self.review_dao.create_review(review)

    def list_reviews(self):
        return self.review_dao.fetch_reviews()

    def find_review(self, review_id: int):
        return self.review_dao.fetch_review_by_id(review_id)

    def delete_review(self, review_id: int):
        return self.review_dao.delete_review(review_id)
