from src.dao.user_dao import UserDAO
from src.model.user import User


class UserService:
    def __init__(self, session):
        self.user_dao = UserDAO(session)

    def register(self, username, password, email, full_name, role="user"):
        user = User(username=username, password=password, email=email, full_name=full_name, role=role)
        return self.user_dao.create_user(user)

    def login(self, username, password):
        return self.user_dao.login(username, password)

    def list_users(self):
        return self.user_dao.fetch_users()

    def delete_user(self, user_id: int):
        return self.user_dao.delete_user(user_id)
