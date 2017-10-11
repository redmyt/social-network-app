

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=gl@c5s5v@v25q6z6*admntr89qez-cyk%o&r2=)8cg#-(_phn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'social_network',
        'USER': 'social_network_user',
        'PASSWORD': 'JaNa0#0%',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}


