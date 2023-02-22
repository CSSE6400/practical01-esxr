# create a Flask project with health
from flask import Flask

def create_app():
    app = Flask(__name__)

    # register routes folder as a blueprint
    from .views.routes import api
    app.register_blueprint(api)

    return app

