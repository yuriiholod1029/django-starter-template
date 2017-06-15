#!/bin/bash -eux

# wait max 5 minutes for db container will be up
./home/docker/code/wait-for-it.sh db:3306 -t 300
# migrate database to current schema, if necessary
python /home/docker/code/app/manage_prod.py migrate
# collect static files
python /home/docker/code/app/manage_prod.py collectstatic --noinput
# run uwsgi processes
uwsgi --ini /home/docker/code/uwsgi.ini
