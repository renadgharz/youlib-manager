from flask import Flask
from launch.launch import launch_blueprint
from auth.auth import auth_blueprint
from config import config
from extensions import db, login_manager, bcrypt

app = Flask(__name__)
app.config.update(config)

db.init_app(app)
login_manager.init_app(app)
bcrypt.init_app(app)

app.register_blueprint(launch_blueprint)
app.register_blueprint(auth_blueprint, url_prefix = "/auth/")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run()