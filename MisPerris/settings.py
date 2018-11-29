"""
Django settings for MisPerris project.

Generated by 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wg&9o=&k#=rz3g1=q1d06o0=yz4z(i2h19(_@@l!0lmio%u)(w'
PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'Back/static/js', 'serviceworker.js')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
    'Back.apps.BackConfig',
    'rest_framework',
    'api.apps.ApiConfig',
    'pwa',


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'MisPerris.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
                
            ],
        },
    },
]

WSGI_APPLICATION = 'MisPerris.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(os.path.dirname(os.path.dirname(__file__)) + "/Back/" ,'static', 'media')

STATIC_ROOT = os.path.join(os.path.dirname(os.path.dirname(__file__))+ "/Back/" ,'static', 'static-only')

STATICFILES_DIRS = (
    os.path.join(os.path.dirname(os.path.dirname(__file__))+ "/Back/" ,'static', 'static'),
)

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(os.path.dirname(__file__))+ "/Back/" ,'static', 'templates'),
)

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'manuel.moreno.cofre@gmail.com'
EMAIL_HOST_PASSWORD = 'Manumatador/123'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

#profe no se meta a mi correo xd saludos

#LOGIN SOCIAL 


AUTHENTICATION_BACKENDS = (
  
  'django.contrib.auth.backends.ModelBackend',
  'social_core.backends.facebook.FacebookOAuth2',
  'social_core.backends.google.GoogleOAuth2',
   'social_core.backends.github.GithubOAuth2',
   'social_core.backends.linkedin.LinkedinOAuth2',
)

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/Mascota/'


SOCIAL_AUTH_GITHUB_KEY = '01ac16347b947e467c72'
SOCIAL_AUTH_GITHUB_SECRET = '8e13bbcd803b9ce97debeaa767b8a81e06b835be'

SOCIAL_AUTH_FACEBOOK_KEY = '728766520832108'  
SOCIAL_AUTH_FACEBOOK_SECRET = '93e33084dd0f48fff1ae9ad649faff28'  

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '672716064650-ucae1rtv8mp35kqdbq185iv82apei6ar.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET= 'nwLVqHVVOZpX9Zqq3na90smb'

SOCIAL_AUTH_TWITTER_KEY = 'NyDdXvA0eZ486Y2rsCvOfwSpe'
SOCIAL_AUTH_TWITTER_SECRET = 'R2PL10JTLguGVm7qqdqZKPqMA1HCoKSEOksyBbxBnL51SHyYrq'

SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY = '86qv2kzjr115v2'
SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET = 'NkI4n5CePB7RXGnC'
