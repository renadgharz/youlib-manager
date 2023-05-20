from flask import Blueprint, render_template

launch_blueprint = Blueprint(
    "launch_blueprint", 
    __name__,
    template_folder='templates',
    static_folder="static"
    )

@launch_blueprint.route('/')
def launch():
    return render_template('launch.html')