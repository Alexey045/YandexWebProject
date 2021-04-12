from flask import Flask, render_template
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def point():
    render_template('base.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

