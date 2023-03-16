from flask import Flask, render_template
from data import db_session
from data.users import User
from data.jobs import Jobs
#from data.departments import Department

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
    


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')