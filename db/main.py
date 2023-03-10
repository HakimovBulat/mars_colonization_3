from flask import Flask
from data import db_session
from data.users import User


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    #app.run()
    user_1 = User()
    user_1.surname = 'Scott'
    user_1.name = 'Ridley'
    user_1.age = 21
    user_1.position = 'captain'
    user_1.speciality = 'research engineer'
    user_1.address = 'module_1'
    user_1.email = 'scott_chief@mars.org'
    db_sess = db_session.create_session()
    db_sess.add(user_1)

    user_2 = User()
    user_2.surname = 'Cameron'
    user_2.name = 'James'
    user_2.age = 35
    user_2.position = 'assistant captain'
    user_2.speciality = 'scientist'
    user_2.address = 'module_2'
    user_2.email = 'james_avatar@pandora.org'
    db_sess.add(user_2)

    user_3 = User()
    user_3.surname = 'Villeneuve'
    user_3.name = 'Denis'
    user_3.age = 45
    user_3.position = 'cook'
    user_3.speciality = 'cooker'
    user_3.address = 'module_2'
    user_3.email = 'denis_worm@dune.org'
    db_sess.add(user_3)

    user_4 = User()
    user_4.surname = 'Lucas'
    user_4.name = 'George'
    user_4.age = 26
    user_4.position = 'doctor'
    user_4.speciality = 'biology teacher'
    user_4.address = 'module_1'
    user_4.email = 'lucas_skywalker@tatuin.org'
    db_sess.add(user_3)
    db_sess.commit()


if __name__ == '__main__':
    main()