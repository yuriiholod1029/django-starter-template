import os
from .base import *  # noqa

import dj_database_url

DEBUG = False

# DATABASE SETTINGS
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

# https://docs.djangoproject.com/en/1.10/ref/settings/#allowed-hosts
ALLOWED_HOSTS = [os.environ['ALLOWED_HOST']]

DB_CONNECTION = dj_database_url.config()
DB_CONNECTION['OPTIONS'] = {
    # utf8mb4 mysql mess: http://stackoverflow.com/a/20349552/95920
    'init_command': "SET sql_mode='STRICT_TRANS_TABLES', storage_engine=INNODB, " +\
                    "character_set_connection=utf8, collation_connection=utf8mb4_general_ci",
    'charset': 'utf8mb4',
}

DATABASES = {
    'default': DB_CONNECTION
}

# IMPORTANT!:
# You must keep this secret, you can store it in an
# environment variable and set it with:
# export SECRET_KEY="phil-dunphy98!-bananas12"
# https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/#secret-key
SECRET_KEY = os.environ['SECRET_KEY']

# WSGI SETTINGS
# https://docs.djangoproject.com/en/1.10/ref/settings/#wsgi-application
WSGI_APPLICATION = 'project.wsgi.application'

# NOTIFICATIONS
# A tuple that lists people who get code error notifications.
# https://docs.djangoproject.com/en/1.10/ref/settings/#admins
ADMINS = (
         ('Your Name', 'your_email@example.com'),
)
MANAGERS = ADMINS

# DJANGO-COMPRESSOR SETTINGS
COMPRESS_PRECOMPILERS = (
    ('text/less', 'lessc {infile} {outfile}'),
)

STATICFILES_FINDERS = STATICFILES_FINDERS + (
    'compressor.finders.CompressorFinder',
)

try:
    from local_settings import * # noqa
except ImportError:
    pass
