from .base import * # noqa

DEBUG = True

SECRET_KEY = 'secret-key'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': base_dir_join('db.sqlite3'),
    }
}

DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

INSTALLED_APPS += ('naomi',)
EMAIL_BACKEND = 'naomi.mail.backends.naomi.NaomiBackend'
EMAIL_FILE_PATH = base_dir_join('tmp_email')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(levelname)-8s [%(asctime)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO'
        },
        'celery': {
            'handlers': ['console'],
            'level': 'INFO'
        }
    }
}