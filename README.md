
### How to use
Create project with virtual environment

1. download files from this repo
2. add virtual environment files
```console
$ python3 -m venv venv
```
3. activate the virual environment 
```console
$ . venv/bin/activate
```

or on Windows
```console
venv\Scripts\activate
```
4. install Flask
```console
$ pip install Flask
$ pip install Flask-SQLAlchemy
```

Set environment variables in terminal
```console
$ export FLASK_APP=app.py
$ export FLASK_ENV=development
```

or on Windows
```console
$ set FLASK_APP=app.py
$ set FLASK_ENV=development
```

Run the app
```console
$ flask run
```