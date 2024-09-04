import os 
from .settings import *  # Change this line
from .settings import BASE_DIR  # Change this line


SECRET_KEY = os.environ['SECRET']
ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']]
CSRF_TRUSTED_ORIGINS = ['https://' + os.environ['WEBSITE_HOSTNAME']]
DEBUG = False

# WhiteNoise configuration
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
] 

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Get the connection string from environment variables
conn_str = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']

# Initialize an empty dictionary to hold the connection string parameters
conn_str_params = {}

# Split the connection string into pairs and process each one
for pair in conn_str.split(' '):
    if '=' in pair:
        key, value = pair.split('=', 1)  # Split on the first '=' only
        conn_str_params[key] = value
    else:
        print(f"Warning: Skipping malformed pair: {pair}")

# Define the DATABASES dictionary for Django
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': conn_str_params.get('dbname'),
        'HOST': conn_str_params.get('host'),
        'USER': conn_str_params.get('user'),
        'PASSWORD': conn_str_params.get('password'),
    }
}
