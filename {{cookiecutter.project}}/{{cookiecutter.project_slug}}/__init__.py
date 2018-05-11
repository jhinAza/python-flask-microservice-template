from flask import Flask
from {{cookiecutter.project_slug}}.{{cookiecutter.project_slug}}_root import {{cookiecutter.project_slug}}

__author__ = """{{cookiecutter.mantainer_name}}"""
__email__ = '{{cookiecutter.mantainer_email}}'
__version__ = '0.1.0'


def create_app():
    app = Flask(__name__)
    app.register_blueprint({{cookiecutter.project_slug}})
    return app
