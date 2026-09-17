from sqlalchemy import select
from src.exception.resource_not_found_exception import ResourceNotFoundException
from src.model.user import User

class UserDAO:
    def __init__(self, session):
        self.session = session

    def create_user(self, u: User):
        try:
            self.session.add(u)
            self.session.flush()
            self.session.commit()
            return u
        except Exception:
            self.session.rollback()
            raise

    def fetch_users(self):
        statement = select(User)
        return self.session.execute(statement).scalars().all()

    def fetch_user_by_id(self, uid: int):
        user = self.session.get(User, uid)
        if not user:
            raise ResourceNotFoundException("User not found")
        return user

    def login(self, username, password):
        statement = select(User).where((User.username == username) & (User.password == password))
        return self.session.execute(statement).scalars().first()

    def delete_user(self, uid: int):
        db_user = self.session.get(User, uid)
        if not db_user:
            raise ResourceNotFoundException("User not found")
        try:
            self.session.delete(db_user)
            self.session.commit()
            return db_user
        except Exception:
            self.session.rollback()
            raise
