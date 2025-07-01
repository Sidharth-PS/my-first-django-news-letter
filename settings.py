# settings.py

import os
from pathlib import Path
import base64

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = True
ALLOWED_HOSTS = ['*']

SECRET_KEY = 'TURSe2g0cmRjMGQzZF9zM2NyM3RfazN5X3BsNV9kMG50X2MwbW0xdH0='

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_URL = '/static/'
