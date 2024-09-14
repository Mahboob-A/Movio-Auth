from .base import *  # noqa
from .base import env  # noqa: E501


SECRET_KEY = env("DJANGO_SECRET_KEY")

# ########################## Security Settings

DEBUG = False 

ALLOWED_HOSTS = ["127.0.0.1"]


CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1:8000",
    "http://127.0.0.1:8080",
]

CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:8000",
    "http://127.0.0.1:8080",
]


############################ ADDED SETTINGS ###############################

# ########################## Static and Media Settings

STATIC_URL = "/static/"
STATIC_ROOT = str(BASE_DIR / "staticfiles")

MEDIA_URL = "/media/"
MEDIA_ROOT = str(BASE_DIR / "mediafiles")

# ########################## Admin URL

ADMIN_URL = env("ADMIN_URL")

# ########################## Auth and DRF Settings

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "dj_rest_auth.jwt_auth.JWTAuthentication",  # JWTAuthentication  JWTCookieAuthentication
    ],
}

# ########################## DJ Rest AUTH Settings
REST_AUTH = {
    "USE_JWT": True,
    "JWT_AUTH_HTTPONLY": False,  # to get refresh token.
    "JWT_AUTH_COOKIE": "movio-access-token",
    "JWT_AUTH_REFRESH_COOKIE": "movio-refresh-token",
    "JWT_TOKEN_CLAIMS_SERIALIZER": "core_apps.users.serializers.CustomTokenObtainPairSerializer",  # some additional data are inluced in the claim
}


SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("Bearer",),
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=43200),  # 30 days 
    "REFRESH_TOKEN_LIFETIME": timedelta(days=30),
    "ROTATE_REFRESH_TOKENS": True,
    "SIGNING_KEY": env("JWT_SIGNING_KEY"),
    "USER_ID_FIELD": "id",
    "USER_IF_CLAIM": "user_id",
}

# ##################### Auth Backends

AUTHENTICATION_BACKENDS = [
    "core_apps.users.auth_backend.EmailAndUsernameCredentialAuthBackend",
    "django.contrib.auth.backends.ModelBackend",
]

# ##################### CORS Config

CORS_URLS_REGEX = r"^api/.*$"

# ##################### User Model

AUTH_USER_MODEL = "users.CustomUser"


# ##################### Networking

DJANGO_APP_PORT = env("DJANGO_APP_PORT")


########################################################
# logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    "formatters": {
        "verbose": {
            "format": "%(levelname)s  %(asctime)s %(module)s  %(process)d %(thread)d %(message)s "
        }
    },
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "root": {
        "level": "INFO",
        "handlers": ["console"],
    },
    "loggers": {
        "django.request": {  # only used when debug=false
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
        "django.security.DisallowedHost": {  # only used when debug=false
            "handlers": ["console", "mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
    },
    # uncomment for django database query logs
    # 'loggers': {
    #     'django.db': {
    #         'level': 'DEBUG',
    #         'handlers': ['console'],
    #     }
    # }
}
