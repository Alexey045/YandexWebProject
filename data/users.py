import sqlalchemy
from werkzeug.security import generate_password_hash, check_password_hash

from data.db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'Users'

    Login = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    Name = sqlalchemy.Column(sqlalchemy.String, index=True, nullable=False)

    PasswordHash = sqlalchemy.Column(sqlalchemy.String)

    Status = sqlalchemy.Column(sqlalchemy.Integer)

    def set_password(self, password):
        self.PasswordHash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)
