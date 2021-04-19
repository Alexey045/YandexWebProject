import sqlalchemy
from sqlalchemy import ForeignKey

from data.db_session import SqlAlchemyBase
from sqlalchemy.orm import relationship


class CartProduct(SqlAlchemyBase):
  __tablename__ = 'CartsProduct'

  Id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

  OwnerCart = sqlalchemy.Column(sqlalchemy.String, ForeignKey('Carts.id'), index=True, nullable=False)
  Owner = relationship('Cart')

  ProductId = sqlalchemy.Column(sqlalchemy.Integer, ForeignKey('Product.Id'), nullable=False)
  Product = relationship('Product')

  Status = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)

  RealTimePrice = sqlalchemy.Column(sqlalchemy.REAL, ForeignKey('Product.Price'), nullable=False)
  RealTimePriceRelation = relationship('')

  PayTimePrice = sqlalchemy.Column(sqlalchemy.REAL)

  Date = sqlalchemy.Column(sqlalchemy.DATE)

