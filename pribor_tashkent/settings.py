"""
Django settings for pribor_tashkent project.

Generated by 'django-admin startproject' using Django 5.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_s@f$)36h9x((t^5(%%8m5f40$2$e^p--q$i$83h^#f+ihm1=1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['api.pribortashkent.uz', 'localhost', '0.0.0.0']


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'drf_spectacular',
    'rest_framework',
    'carousel',
    'catalog',
    'tinymce',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pribor_tashkent.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'pribor_tashkent.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static/'

MEDIA_ROOT = BASE_DIR / 'media/'
MEDIA_URL = '/media/'


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


JAZZMIN_UI_TWEAKS = {
    "theme": "pulse",
}


JAZZMIN_SETTINGS = {
    "site_title": "Tashkent Pribor Admin",
    "site_header": "Tashkent Pribor",
    "site_brand": "Tashkent Pribor",


    "login_logo": None,


    "login_logo_dark": None,

    "site_icon": None,

    "welcome_sign": "Tashkent Pribor Admin",
    "copyright": "Tashkent Pribor Ltd",
    "order_with_respect_to": ["maps_app"],
}

TINYMCE_DEFAULT_CONFIG = {
    "height": 600,  # Высота редактора
    "width": "100%",  # Ширина редактора
    "plugins": (
        "advlist autolink lists link image charmap print preview anchor "
        "searchreplace visualblocks code fullscreen insertdatetime media table "
        "paste code help wordcount emoticons fullscreen hr pagebreak "
        "imagetools textcolor codesample"
    ),
    "toolbar": (
        "undo redo | formatselect | bold italic underline strikethrough | "
        "alignleft aligncenter alignright alignjustify | "
        "bullist numlist outdent indent | link image media | "
        "forecolor backcolor | codesample code | table emoticons | fullscreen"
    ),
    "menubar": "file edit view insert format tools table help",  # Включение меню
    # "file_picker_callback": "function (callback, value, meta) { ... }",  # Поддержка выбора файлов
    "image_advtab": True,  # Расширенные настройки для изображений
    "imagetools_toolbar": "rotateleft rotateright | flipv fliph | editimage imageoptions",
    "automatic_uploads": True,  # Автоматическая загрузка
    "file_picker_types": "image media file",  # Разрешить выбор изображений
    "relative_urls": False,  # Абсолютные ссылки
    "remove_script_host": False,  # Удаление хоста из ссылок
    "content_style": "body { font-family:Arial,Helvetica,sans-serif; font-size:14px }",  # Стили для контента
    "codesample_languages": [  # Подсветка кода
        {"text": "Python", "value": "python"},
        {"text": "HTML/XML", "value": "markup"},
        {"text": "JavaScript", "value": "javascript"},
        {"text": "CSS", "value": "css"},
    ],
    "language": "ru",
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'PriborTashkent API',
    'DESCRIPTION': 'API for PriborTashkent',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': True,
    'COMPONENT_SPLIT_REQUEST': True,
    # OTHER SETTINGS
}
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

CORS_ORIGIN_ALLOW_ALL = True
SECURE_CROSS_ORIGIN_OPENER_POLICY = "same-origin-allow-popups"

CSRF_TRUSTED_ORIGINS = [
    'https://api.pribortashkent.uz'
]
