from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = "django-insecure-r$ne8$0a$3und5&+#+e_ga(5q57#mud#4h1z-6092=0j(8(_@g"
DEBUG = True
ALLOWED_HOSTS = []
INSTALLED_APPS = [
    "django_fernet",
    "testapp",
]
MIDDLEWARE = [
    "django.middleware.common.CommonMiddleware",
]
ROOT_URLCONF = "testapp.urls"
WSGI_APPLICATION = "testapp.wsgi.application"
DATABASES = {
    "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": BASE_DIR / "db.sqlite3"},
}
LANGUAGE_CODE = "de-at"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
