import sqlalchemy
from data.db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'Users'

    Login = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    Name = sqlalchemy.Column(sqlalchemy.String, index=True, nullable=False)

    PasswordHash = sqlalchemy.Column(sqlalchemy.String)

    Status = sqlalchemy.Column(sqlalchemy.Integer)
