from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.login import LoginManager
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object("config")
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager()
bootstrap = Bootstrap(app)
from app import views, models
from .auth import auth as auth_blueprint

app.register_blueprint(auth_blueprint, url_prefix='/auth')
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
login_manager.init_app(app)


