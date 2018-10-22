from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, PasswordField, ValidationError
from wtforms.fields.html5 import EmailField
from app_blog.author.model import UserReister


class FormRegister(FlaskForm):
    """依照Model來建置相對應的Form
    
    password2: 用來確認兩次的密碼輸入相同
    """
    username = StringField('UserName', validators=[
        validators.DataRequired(),
        validators.Length(10, 30)
    ])
    email = EmailField('Email', validators=[
        validators.DataRequired(),
        validators.Length(1, 50),
        validators.Email()
    ])
    password = PasswordField('PassWord', validators=[
        validators.DataRequired(),
        validators.Length(5, 10),
        validators.EqualTo('password2', message='PASSWORD NEED MATCH')
    ])
    password2 = PasswordField('Confirm PassWord', validators=[
        validators.DataRequired()
    ])
    submit = SubmitField('Register New Account')

    def validate_email(self, field):
        if UserReister.query.filter_by(email=field.data).first():
            raise ValidationError('Email already register by somebody')

    def validate_username(self, field):
        if UserReister.query.filter_by(username=field.data).first():
            raise ValidationError('UserName already register by somebody')
