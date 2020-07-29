import os

from .base import *
from .installed import *

HOME_PAGE_MSG = "Hello world this is local"

print("Using local")
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
