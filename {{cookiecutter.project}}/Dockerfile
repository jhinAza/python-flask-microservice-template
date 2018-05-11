FROM python:3.6

MAINTAINER {{cookiecutter.mantainer_name}} "{{cookiecutter.mantainer_email}}"

# Install requirements
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /usr/src/{{cookiecutter.project}}
ENV PYTHONPATH /usr/src/{{cookiecutter.project}}

WORKDIR /usr/src/{{cookiecutter.project}}

COPY . /usr/src/{{cookiecutter.project}}/
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT gunicorn -b 0.0.0.0:{{cookiecutter.port}} 'main:app'
