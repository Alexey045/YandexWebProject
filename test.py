from flask import Flask, render_template
from werkzeug.utils import redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


app = Flask(__name__)
app.config['SECRET_KEY'] = "My little strange password that i don`t understand"


@app.route('/')
def test():
    return render_template('base.html')


@app.route('/success')
def third():
    return 'success'
    # return render_template('3.html')


@app.route('/registration')
def registration():
    return render_template('registration.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
