from app_blog import app
from app_blog import db
from flask import render_template
from app_blog.author.model import UserRegister
from app_blog.author.form import FormRegister
from app_blog.sendmail import send_mail


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = FormRegister()

    if form.validate_on_submit():
        user = UserRegister(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data
        )
        db.session.add(user)
        db.session.commit()
        #  產生用戶認證令牌
        token = user.create_confirm_token()
        #  寄出帳號啟動信件
        send_mail(sender='Sender@domain.com',
                  recipients=['recipients@domain.com'],
                  subject='Activate your account',
                  template='author/mail/welcome',
                  mailtype='html',
                  user=user,
                  token=token)

        return 'Check Your Email and Activate Your Account'
    return render_template('author/register.html', form=form)


@app.route('/user_confirm/<token>')
def user_confirm(token):
    user = UserRegister()
    data = user.validate_confirm_token(token)
    if data:
        user = UserRegister.query.filter_by(id=data.get('user_id')).first()
        user.confirm = True
        db.session.add(user)
        db.session.commit()
        return 'Thands For Your Activate'
    else:
        return 'wrong token'