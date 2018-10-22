from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from config import Config
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

#  很重要，一定要放這邊
from app_blog.author import view