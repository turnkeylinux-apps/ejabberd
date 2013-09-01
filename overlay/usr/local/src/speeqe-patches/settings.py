# Django settings for speeqeweb project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Admin', 'admin@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/var/lib/sqlite/speeqe.db',
        'USER': '',
        'PASSWORD': '',
    }
}

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
USE_I18N = True

SITE_ID = 1
SECRET_KEY = '2n0d+c94i^@$+dsx7@t0d-_at=p@lyk8f23&bn3m$s6e8or)x4'

ADMIN_MEDIA_PREFIX = '/admin_media/'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
)

ROOT_URLCONF = 'speeqeweb.urls'

MEDIA_ROOT = '/var/www/django/speeqeweb/webroot'
DOCUMENT_ROOT = '/var/www/django/speeqeweb/webroot'

TEMPLATE_DIRS = (
    'templates',
    '/var/www/django/speeqeweb/templates',
    '/var/www/django/speeqeweb/webroot',
    '/var/www/django/speeqeweb/webroot/speeqewebclient',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'speeqeweb.speeqe',
    'speeqeweb.avatars',
)


## Speeqe configuration settings

HTTP_DOMAIN = "chat.example.com"
XMPP_DOMAIN = "example.com"

SESSION_COOKIE_DOMAIN = ".example.com"
HELP_EMAIL = 'support@example.com'
LOG_ROOT = '/var/log/speeqe'

# Exact and matching words to/in usernames to reject
EXACT_BAD_WORDS = ['']
MATCH_BAD_WORDS = ['']

# Robot user to list active rooms from the muc component (disco requests)
XMPP_USER = 'robot@example.com'
XMPP_PASS = 'turnkey'
XMPP_CHAT = 'conference.example.com'

# Bosh server details
BOSH_HOST = "127.0.0.1"
BOSH_PORT = "5280"
BOSH_URL = "/http-bind"

# MUC rooms to list on the front page (/room/ or use dns trick)
FEATURED_ROOMS = {'Alpha Room':'/room/alpha/', 'Beta Room':'/room/beta/', }

# Mail server configuration
SMTP_SERVER = '127.0.0.1'
SMTP_PORT = 25

# Avatar settings
AVATAR_DEFAULT_SHA1 = 'f2f8ab835b10d66f9233518d1047f3014b3857cf'
AVATAR_DEFAULT_IE6 = 'b04b0e215af8ce2b7d620aaef32492c8bfc06ed5'
AVATAR_DEFAULT_DIMENSIONS = '30|30'
AVATAR_CACHE_TIMEOUT = 6000

# Allow django to serve all unknown urls as static data
SERVE_STATIC_URLS = True

# Use the DNS trick (alpha.example.com instead of example.com/room/alpha)
DNS_ROOM_NAMES = False

