from .base import *  # noqa
from .base import env

SESSION_COOKIE_AGE = 60 * 60 * 24  # 24 hours
SESSION_COOKIE_SECURE = True

SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = ["localhost"] + env.list("ALLOWED_HOST")

ADMINS = [el.split(":") for el in env.list("DJANGO_ADMINS", default=[])]

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_PORT = env("EMAIL_PORT")
EMAIL_USE_TLS = env("EMAIL_USE_TLS")