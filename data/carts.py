import sqlalchemy
from sqlalchemy import ForeignKey

from data.db_session import SqlAlchemyBase
from sqlalchemy.orm import relationship


class Cart(SqlAlchemyBase):
  __tablename__ = 'Carts'

  Id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

  OwnerLogin = sqlalchemy.Column(sqlalchemy.String, ForeignKey('Users.Login'), index=True, nullable=False)
  Owner = relationship('User')