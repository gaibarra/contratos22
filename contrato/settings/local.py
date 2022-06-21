from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

ALLOWED_HOSTS = ['*']



# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.postgresql_psycopg2',
         'NAME': 'contrato',
         'HOST': 'localhost',
         'USER': 'postgres',
         'PASSWORD': '6Vlgpcr/zaira',
         'PORT': 5434
     }
 }

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/


STATIC_ROOT= os.path.join(BASE_DIR,'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR,'static'),)