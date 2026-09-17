from sqlalchemy import select
from src.exception.resource_not_found_exception import ResourceNotFoundException
from src.model.review import Review

class ReviewDAO:
    def __init__(self, session):
        self.session = session

    def create_review(self, r: Review):
        try:
            self.session.add(r)
            self.session.flush()
            self.session.commit()
            return r
        except Exception:
            self.session.rollback()
            raise

    def fetch_reviews(self):
        statement = select(Review).join(Review.user).join(Review.movie)
        return self.session.execute(statement).scalars().all()

    def fetch_review_by_id(self, rid: int):
        review = self.session.get(Review, rid)
        if not review:
            raise ResourceNotFoundException("Review not found")
        return review

    def delete_review(self, rid: int):
        db_review = self.session.get(Review, rid)
        if not db_review:
            raise ResourceNotFoundException("Review not found")
        try:
            self.session.delete(db_review)
            self.session.commit()
            return db_review
        except Exception:
            self.session.rollback()
            raise
