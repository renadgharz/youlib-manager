from flask import Flask
from launch.launch import launch_blueprint
from auth.auth import auth_blueprint
from config import config

import logging
from logging.handlers import RotatingFileHandler


app = Flask(__name__)

app.config.update(config)

app.register_blueprint(launch_blueprint)
app.register_blueprint(auth_blueprint, url_prefix = "/auth/")

logging_handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
logging_handler.setLevel(logging.INFO)
app.logger.addHandler(logging_handler)


if __name__ == "__main__":
    app.run()