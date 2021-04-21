from data import db_session
from data.carts import Cart
from data.carts_product import CartProduct
from data.category import Category
from data.product import Product
from data.product_category import ProductCategory
from data.users import User


def get_all_categorys():
    db_sess = db_session.create_session()
    return db_sess.query(Category).all()


def get_all_products_with_category(categorys):
    db_sess = db_session.create_session()
    ProductCategoryList = None
    for i in categorys:
        if not ProductCategoryList:
            ProductCategoryList = db_sess.query(ProductCategory.ProductId).filter(ProductCategory.CategoryId == i.Id)
        else:
            ProductCategoryList = ProductCategoryList.filter(ProductCategory.CategoryId == i.Id)
    ProductCategoryList = ProductCategoryList.all()[0]
    Products = db_sess.query(Product).all()
    Access = []
    for i in Products:
        if i.Id in ProductCategoryList:
            Access.append(i)
    return Access


if __name__ == '__main__':
    db_session.global_init("../db/database.db")
    print(get_all_products_with_category((get_all_categorys()[0], )))