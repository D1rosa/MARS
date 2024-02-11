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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')