from flask import Flask, render_template, request
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect
from forms import RegisterForm, LoginForm
from data import db_session

check = False  # ToDo


# from data.users import User


def set_password(self, password):
    self.hashed_password = generate_password_hash(password)


def check_password(self, password):
    return check_password_hash(self.hashed_password, password)


app = Flask(__name__)
app.config['SECRET_KEY'] = "My little strange password that i don`t understand"


@app.route('/')
def base():
    return render_template('base.html', title='Главная страница')


@app.route('/success')
def success():
    return 'success'


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('registration.html',
                                   form=form,
                                   message="Пароли не совпадают!")
        """user = {"name": form.name.data,
                "email": form.email.data,
                "password": form.password.data}"""
        # user.set_password(form.password.data) for db
        return redirect('/')
    return render_template('registration.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # print(request.form.get('remember_me')) y - check true. None - check false
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form, check=check)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
