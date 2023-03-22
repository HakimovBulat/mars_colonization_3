from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField, IntegerField, DateField
from wtforms.validators import DataRequired


class JobForm(FlaskForm):
    team_leader = IntegerField('id руководителя', validators=[DataRequired()])
    job = StringField('Описание работы', validators=[DataRequired()])
    work_size = IntegerField('Объем работы в часах', validators=[DataRequired()])
    collaborators = StringField('Cписок id участников', validators=[DataRequired()])
    start_date = DateField('Дата начала', validators=[DataRequired()])
    end_date = DateField('Дата окончания', validators=[DataRequired()])
    is_finished = BooleanField('Работа завершена', validators=[DataRequired()])