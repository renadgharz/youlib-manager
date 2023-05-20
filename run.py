from flask import Flask
from launch.launch import launch_blueprint

app = Flask(__name__)
app.register_blueprint(launch_blueprint)

if __name__ == "__main__":
    app.run(debug=True)