from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FileField, EmailField, RadioField
from wtforms.validators import DataRequired


class JobPostForm(FlaskForm):
    company_name = StringField('Company Name', validators=[DataRequired()])
    desired_major = StringField('Desired Major', validators=[DataRequired()])
    job_title = StringField('Job Title', validators=[DataRequired()])
    job_desc = StringField('Job Description', validators=[DataRequired()])
    more_info = FileField('Job Flyer')
    email = EmailField('Email', validators=[DataRequired()])
    position = RadioField('Position', choices=[('Full-Time','Full-Time'),('Part-Time','Part-Time'),('Internship','Internship')], validators=[DataRequired()])
    submit = SubmitField('Post')
