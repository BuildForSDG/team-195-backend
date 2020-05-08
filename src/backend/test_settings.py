from .settings import DATABASES

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'test',
        'USER': 'postgres',
        'PASSWORD': 'team-195',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
