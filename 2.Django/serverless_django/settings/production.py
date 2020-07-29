import os

from .base import *
from .installed import *

HOME_PAGE_MSG = "Hello world this is prod"

ALLOWED_HOSTS = ['*']
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY =  os.environ.get("SECRET_KEY",'oegf*v#r7p49c3-65bw7bli-^5ou4f8gl4gs3e0t5ds113duxg')

print("Using prod")
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db_prod.sqlite3'),
    }
}
