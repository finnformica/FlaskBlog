from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config

mail = Mail()        # initialise Mail object for password reset
db = SQLAlchemy()    # initialise database object for storing user data
bcrypt = Bcrypt()    # initialise encryption object for hashing passwords
login_manager = LoginManager() # initliase flask-login to log users in and out

login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

def create_app(config_class=Config):
    app = Flask(__name__)   # initialise Flask app
    app.config.from_object(Config) # configure Flask object using Config class

    mail.init_app(app)
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    # import and initialise Flask blueprints from packages
    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main
    from flaskblog.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app
