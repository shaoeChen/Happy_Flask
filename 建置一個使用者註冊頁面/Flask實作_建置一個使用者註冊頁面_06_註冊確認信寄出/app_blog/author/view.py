from app_blog import app
from app_blog import db
from flask import render_template
from app_blog.author.model import UserReister
from app_blog.author.form import FormRegister
from app_blog.sendmail import send_mail


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = FormRegister()

    if form.validate_on_submit():
        user = UserReister(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data
        )
        db.session.add(user)
        db.session.commit()

        #  寄出帳號啟動信件
        send_mail(sender='Sender@domain.com',
                  recipients=['recipients@domain.com'],
                  subject='Activate your account',
                  template='author/mail/welcome',
                  mailtype='html',
                  user=user)

        return 'Check Your Email and Activate Your Account'
    return render_template('author/register.html', form=form)