from flask import Flask, render_template  # request
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect
from data import db_session
from data.users import User
from forms import RegisterForm, LoginForm


# from flask_login import LoginManager, login_user, login_required, logout_user


# from data.users import User


def set_password(self, password):
    self.hashed_password = generate_password_hash(password)


def check_password(self, password):
    return check_password_hash(self.hashed_password, password)


app = Flask(__name__)
app.config['SECRET_KEY'] = "My little strange password that i don`t understand"


# login_manager = LoginManager()
# login_manager.init_app(app)


@app.route('/')
def base():
    return render_template('main.html', title='Главная страница')


"""@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)"""


@app.route('/success')
def success():
    return 'success'


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('registration.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.Login == form.email.data).first():
            return render_template('registration.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            Name=form.name.data,
            Login=form.email.data,
            PasswordHash=form.password.data,
            Status=0
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('registration.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # print(request.form.get('remember_me')) y - check true. None - check false
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


"""
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)"""

"""
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")"""


@app.route('/about')
def about():
    return render_template('about.html', title='О нас')


@app.route('/developers')
def developers():
    return render_template('developers.html', title='Разработчики')


if __name__ == '__main__':
    db_session.global_init("db/database.db")
    app.run(port=8080, host='127.0.0.1')
