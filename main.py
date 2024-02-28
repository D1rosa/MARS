from flask import Flask, url_for, request, render_template, json, redirect
# from login import LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof)


@app.route('/list_prof')
def list_prof():
    return render_template('list_prof.html',)


@app.route('/answer')
def answer():
    pass
    return render_template('login.html',)


@app.route('/auto_answer')
def auto_answer():
    pass
    return render_template('login.html',)


@app.route('/login')
def login():
    return render_template('login.html',)


@app.route('/distribution')
def distribution():
    p = ['Астронавт', 'Инженер', 'Медик', 'Геолог', 'Химик', 'Физик', 'Математик', 'Программист',
         'Психолог', 'Сантехник', 'Электрик', 'Лидер', 'Учёный', 'Художник', 'Педагог']
    return render_template('distribution.html', people=p)


@app.route('/table/<sex>/<age>')
def table(sex, age):
    return render_template('table.html', sex=sex, age=age)


@app.route('/gallery')
def gallery():
    # carousel + load_files
    return render_template('gallery.html')


@app.route('/member')
def member():
    # анкета + рандом вывод
    return render_template('member.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
