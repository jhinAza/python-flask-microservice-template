from flask import Blueprint, current_app, render_template

{{cookiecutter.project_slug}} = Blueprint("{{cookiecutter.project_slug}}", __name__)

@{{cookiecutter.project_slug}}.route('/')
def root():
    return "Hello world"
