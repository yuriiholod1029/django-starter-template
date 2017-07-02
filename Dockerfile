FROM python:3.5
ENV PYTHONUNBUFFERED 1

# Install dependencies for django-compressor
RUN apt-get update
RUN apt-get install -y node-less yui-compressor

# Install uwsgi, which is only on production requirments.
# It is not neccessary do keep wsgi in requirments.txt
RUN pip install uwsgi

# Install requirments before adding rest of code.
# It is allow to use Docker caching.
ADD app/requirements_prod.txt /home/docker/code/app/
RUN pip install -r /home/docker/code/app/requirements_prod.txt

# add the rest of code to image
ADD . /home/docker/code/
