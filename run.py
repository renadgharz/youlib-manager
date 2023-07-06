from flask import Flask
from launch.launch import launch_blueprint
from auth.auth import auth_blueprint
from config import config
from extensions import db

app = Flask(__name__)
app.config.update(config)
app.register_blueprint(launch_blueprint)
app.register_blueprint(auth_blueprint, url_prefix = "/auth/")

db.init_app(app)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run()