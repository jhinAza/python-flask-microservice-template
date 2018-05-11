import {{cookiecutter.project_slug}}

app = {{cookiecutter.project_slug}}.create_app()

def main():
    app.run(host="127.0.0.1", port={{cookiecutter.port}}, debug=True)

if __name__ == '__main__':
    main()
