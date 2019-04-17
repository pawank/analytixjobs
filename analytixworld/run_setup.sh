#!/bin/bash - 

brew install pipenv
export PIPENV_VENV_IN_PROJECT=1
pipenv --python 3.7
pipenv install --dev
#Mac OSX
#env LDFLAGS='-L/usr/local/lib -L/usr/local/Cellar/openssl/1.0.2r/lib -L/usr/local/Cellar/readline/8.0.0/lib' pip3.7 install psycopg2
pipenv install Django
pipenv install psycopg2
pipenv install requests
#pipenv run python manage.py startapp users
#pipenv run python manage.py makemigrations users
