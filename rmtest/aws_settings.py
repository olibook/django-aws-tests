DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'rmtest',                      # Or path to database file if using sqlite3.
        'USER': 'ripple',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': 'ip-10-28-182-59.ec2.internal',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '0ripple1',                      # Set to empty string for default. Not used with sqlite3.
    }
}
