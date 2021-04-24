import os
import string
from random import sample, shuffle
from tempfile import SpooledTemporaryFile

from werkzeug.utils import secure_filename

from data import db_session
from data.carts import Cart
from data.carts_product import CartProduct
from data.category import Category
from data.product import Product
from data.users import User


def generate_random_trash(m):
    digits = list(set(string.digits) - {'1', '0'})
    while True:
        c = m // 3
        b = m - 2 * c
        if c <= 8:
            a = sample(digits, c)
        else:
            a = digits
            d = (c - len(digits)) + c + b
            if d % 2 == 0:
                c, b = int(d / 2), int(d / 2)
            else:
                c, b = int(d // 2), int(d // 2 + 1)
        a.extend(sample(digits, c))
        a.extend(sample(digits, b))
        shuffle(a)
        a = ''.join(a)
        if (a + ".jpg" not in os.listdir("./static/img/")) and (
                a + ".png" not in os.listdir("./static/img/")) and (
                a + ".jpeg" not in os.listdir("./static/img/")):
            break
    return a


def get_all_categorys():
    db_sess = db_session.create_session()
    return db_sess.query(Category).all()


def get_all_products_with_category(categorys):
    db_sess = db_session.create_session()
    ProductCategoryList = None
    ProductCategoryList = ProductCategoryList.all()[0]
    Products = db_sess.query(Product).all()
    Access = []
    for i in Products:
        if i.Id in ProductCategoryList:
            Access.append(i)
    return Access


def add_product(name, description, price, count, image, form, res):
    db_sess = db_session.create_session()
    imageid = generate_random_trash(10)
    cat = None
    for categories in res:
        if form.category.data in categories:
            cat = categories[0]
    new_product = Product(Name=name,
                          Description=description,
                          Price=price,
                          Count=count,
                          ImageId=imageid, Category=cat)
    with open(f"./static/img/{imageid}.jpg", "wb") as f:
        f.write(image.data.stream.read())
    db_sess.add(new_product)
    db_sess.commit()


if __name__ == '__main__':
    pass
