.PHONY: docs test coverage build docker-run run help
.DEFAULT_GOAL := help
define BROWSER_PYSCRIPT
import os, webbrowser, sys
try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT
BROWSER := python -c "$$BROWSER_PYSCRIPT"

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/

{% if cookiecutter.test_suite == 'unittest' %}
test: ## run tests quickly using unittest
	PYTHONPATH=. python -m unittest discover tests
{% else %}
test: ## run tests quickly using unittest
	PYTHONPATH=. python -m pytest tests
{% endif %}

coverage: ## check code coverage quickly with the default Python
	PYTHONPATH=. coverage run --source=. -m unittest discover tests
	coverage report --omit=tests/* -m
	coverage html
	$(BROWSER) htmlcov/index.html

docs: ## generate Sphinx HTML documentation, including API docs
	rm -f docs/{{cookiecutter.project_slug}}.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ {{cookiecutter.project_slug}}
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	$(BROWSER) docs/_build/html/index.html

build: ## build docker image
	docker-compose build

docker-run: ## run precompiled docker container
	docker-compose up

run: ## run using debug mode
	python main.py

venv: ## Create python native virtualenv
	python3 -m venv .venv
	chmod u+x .venv/bin/activate

requirements: ## Install requirements in python native virtualenv
	.venv/bin/activate
	pip install -r requirements.txt

dev-requirements: ## Install dev requirements in python native virtualenv
	$(MAKE) requirements
	pip install -r requirements.dev.txt

clean-venv:
	rm -rf .venv
	$(MAKE) venv
