from flask import Flask, render_template, redirect, request
from data import db_session
from data.users import User
from data.jobs import Jobs
from data.userform import UserForm
from flask_login import LoginManager, login_user
from data.loginform import LoginForm


app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_session.global_init("db/blogs.db")


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html', title='Главная страница')


@app.route('/')
@app.route('/work_logs')
def work_logs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    team_leaders = []
    for job in jobs:
        user = db_sess.query(User).filter(User.id == job.team_leader).first()
        team_leaders.append(user.name + ' ' + user.surname)       
    return render_template('work_logs.html', title='Работы', jobs=jobs, team_leaders=team_leaders)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html', message="Неправильный логин или пароль", form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = UserForm()
    if form.validate_on_submit():
        db_session.global_init("db/blogs.db")
        db_sess = db_session.create_session()
        user = User(
            surname=request.form['surname'], name=request.form['name'], 
            email=request.form['username'], age=request.form['age'],
            position=request.form['position'], speciality=request.form['speciality'], 
            address=request.form['address']
                    )
        db_sess.add(user)
        db_sess.commit()
        return redirect('/success')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/success')
def success():
    return render_template('success.html', title='Доступ разрешён')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')