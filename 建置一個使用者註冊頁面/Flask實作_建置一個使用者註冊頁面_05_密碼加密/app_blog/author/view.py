from app_blog import app
from app_blog import db
from flask import render_template
from app_blog.author.model import UserReister
from app_blog.author.form import FormRegister


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
        return 'Success Thank You'
    return render_template('author/register.html', form=form)
