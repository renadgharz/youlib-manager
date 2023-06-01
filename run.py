from flask import Flask
from launch.launch import launch_blueprint
from auth.auth import auth_blueprint
from config import config


app = Flask(__name__)

app.config.update(config)

app.register_blueprint(launch_blueprint)
app.register_blueprint(auth_blueprint)


if __name__ == "__main__":
    app.run()