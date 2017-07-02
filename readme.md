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

## How to dockerized your existing app? ##
    - make app directory in root of your project
    - move to app directory all files from root of your django app (required django 1.10)
    - copy all files from root of this repository except app directory to root of your project
    - in app directory create project directory which should contains:
        - settings folder with settings proper for development 
            (development.py) and production (production.py) 
            We recommend to remain given settings in example app and onlny customize it.
        - static folder with all sataic files (is not necessary, but recommended)
        - files:
            - views.py
            - urls.py (top level django urls)
            - wsgi.py
    - modify following files:
        - rename manage.py to manage_prod.py:
            replace proper line to: 
                os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings.production")
        - copy manage_prod.py and rename to manage_dev.py:
            replace proper line to: 
                os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings.development")
        - wsgi.py:
             replace proper line to: 
                os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings.production")
        - urls.py:
            add: import project.views and remove previous version
        - settings_versions/production.py
            set ROOT_URLCONF = 'project.urls'
            set WSGI_APPLICATION = 'project.wsgi.application'
            set DB_CONNECTION = dj_database_url.config()
                DB_CONNECTION['OPTIONS'] = {
                    # utf8mb4 mysql mess: http://stackoverflow.com/a/20349552/95920
                    'init_command': "SET sql_mode='STRICT_TRANS_TABLES', storage_engine=INNODB, " +\
                                    "character_set_connection=utf8, collation_connection=utf8mb4_general_ci",
                    'charset': 'utf8mb4',
                }
                DATABASES = {
                    'default': dj_database_url.config()
                }
            add import dj_database_url
        - settings_versions/development.py
            set ROOT_URLCONF = 'project.urls'
            set WSGI_APPLICATION = 'project.wsgi.application'
    - add dj_database_url=0.4.2 and mysqlclient to requirments.txt
    - check that application constructed in this way working running it in development mode
      (using python app/manage_dev.py runserver)
    - edit .env file and set your custom credentials (remember to remove secret key from production settings and
      set as env variable defined in this file
   
   After these changes deployment is the same as prevoius points.
