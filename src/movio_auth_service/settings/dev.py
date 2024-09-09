from .base import *  # noqa
from .base import env  # noqa: E501


SECRET_KEY = env("DJANGO_SECRET_KEY")


DEBUG = True 

ALLOWED_HOSTS = ["127.0.0.1"]


CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1:8000",
    "http://127.0.0.1:8080",
]

CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:8000",
    "http://127.0.0.1:8080",
]

########################################################
# logging

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(name)-12s %(asctime)s %(module)s  %(process)d %(thread)d %(message)s "
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "root": {
        "level": "INFO",
        "handlers": ["console"],
    },
    # uncomment for django database query logs
    # 'loggers': {
    #     'django.db': {
    #         'level': 'DEBUG',
    #         'handlers': ['console'],
    #     }
    # }
}
