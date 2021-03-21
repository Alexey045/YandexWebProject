from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    """db_session.global_init("db/blogs.db")
    user1 = User()
    user1.surname = "Scott"
    user1.name = "Ridley"
    user1.age = 21
    user1.position = "captain"
    user1.speciality = "research engineer"
    user1.address = "module_1"
    user1.email = "scott_chief@mars.org"
    db_sess = db_session.create_session()
    db_sess.add_all([user1])
    db_sess.commit()
    # app.run()"""


if __name__ == '__main__':
    main()
