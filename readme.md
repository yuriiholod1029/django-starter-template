# Django project template #

An easy to use project template for django 1.10 with included dockerization for deployment.
<br/>
Based on [fasouto django project template](https://github.com/fasouto/django-starter-template)

## Features ##

- Compatible with python 3.5
- [Docker, Docker Compose](https://www.docker.com/) for fast and easy deployment
- [Django compressor](http://django-compressor.readthedocs.org/en/latest/) to compress JS and CSS and compile LESS/SASS files.
- [Django debug toolbar](http://django-debug-toolbar.readthedocs.org/) enabled for superusers.
- [Argon2](https://docs.djangoproject.com/en/1.10/topics/auth/passwords/#using-argon2-with-django) to hash the passwords

## Set up project for development ##

Create and activate your virtualenv, you can use [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/). Then install Django 1.10 in your virtualenv:

    pip install django==1.10

To create a new django project (make sure to change `project_name` and `path-to-download-zip`)

    django-admin.py startproject --template=path-to-downloaded-zip --extension=py,md,html,txt,less project_name

Change directory to your project and install the dependences

    pip install -r app/requirements_dev.txt

If you need a database (default sqlite), edit the settings and create one with

    python app/manage_dev.py migrate

Once everything it's setup you can run the development server: [http://localhost:8000/](http://localhost:8000/)

    python appp/manage_dev.py runserver

## Working with template ##

Standard commands are changed a little.

To create new app to django project run in root of project (make sure to change `app-name`):

	mkdir app/apps/app-name
	python app/manage_dev.py startapp app-name app/apps/app-name

To make database migration file:

	python app/manage_dev.py makemigrations

To apply migration:

	python app/manage_dev.py migrate

## Deployment for first time ##

On machine for deployment:

Install dependiencies (only on first time):

	sudo apt-get install git docker.io docker-compose

Clone repository with your application and change directory to root of repository
checkout to git branch with version to deployment

Add permisions for execution for deployment scritps:

	chmoud u+x *.sh

Create docker .env file from template:

	cp .env-templatate .env

Customize created .env file

Check that port 80 on ALLOWED_HOST is free.

Run:

	./deploy.sh

to build and run app containers for first deployment

Check docker-compose logs and wait until uwsgi processes run

Check http://ALLOWED_HOST from .env file

## Update of deployed application ##

Fetch new changes from git

checkout to git branch with version to deployment

Run:
 ./update.sh

 for updating django container

check docker-compose logs and wait until uwsgi processes run

check http://ALLOWED_HOST from .env file

## Deployment info ##

Deployed application consists of three connected docker containers:
- database container with installed mariadb
- django container with running uwsgi processes
- http server container with installed nginx

These containers uses volumes binding to host directories defined in .env file
for persisting data.
