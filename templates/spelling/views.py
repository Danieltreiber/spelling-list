from flask import render_template, Blueprint
spelling_blueprint = Blueprint('spelling',__name__)

@spelling_blueprint.route('/')
@spelling_blueprint.route('/spelling')
def index():
    return render_template("index.html")
