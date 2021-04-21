import sqlalchemy
from sqlalchemy import ForeignKey

from data.db_session import SqlAlchemyBase
from sqlalchemy.orm import relationship


class ProductCategory(SqlAlchemyBase):
    __tablename__ = 'ProductCategory'

    Id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    CategoryId = sqlalchemy.Column(sqlalchemy.String, ForeignKey('Category.Id'), index=True, nullable=False)
    Category = relationship('Category')

    ProductId = sqlalchemy.Column(sqlalchemy.Integer, ForeignKey('Product.Id'), nullable=False)
    Product = relationship('Product')
