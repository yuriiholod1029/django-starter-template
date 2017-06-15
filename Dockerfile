FROM python:3.5
ENV PYTHONUNBUFFERED 1

# Install uwsgi, which is only on production requirments.
# It is not neccessary do keep wsgi in requirments.txt
RUN pip install uwsgi

# Install requirments before adding rest of code.
# It is allow to use Docker caching.
ADD app/requirements.txt /home/docker/code/app/
RUN pip install -r /home/docker/code/app/requirements.txt

# add the rest of code to image
ADD . /home/docker/code/
