#!/bin/bash - 

pipenv run python manage.py migrate
#pipenv run python manage.py createsuperuser
pipenv run python manage.py runserver 0.0.0.0:9000
