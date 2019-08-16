from flask import Flask
app = Flask(__name__,
            static_folder = './public',
            template_folder="./static")

from templates.spelling.views import spelling_blueprint

# register the blueprints
app.register_blueprint(spelling_blueprint)