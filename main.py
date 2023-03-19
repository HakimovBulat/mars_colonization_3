from flask import Flask, render_template, redirect, request
from data import db_session
from data.users import User
from data.jobs import Jobs
from data.userform import UserForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/work_logs')
def work_logs():
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    team_leaders = []
    for job in jobs:
        user = db_sess.query(User).filter(User.id == job.team_leader).first()
        team_leaders.append(user.name + ' ' + user.surname)       
    return render_template('work_logs.html', title='Работы', jobs=jobs, team_leaders=team_leaders)


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