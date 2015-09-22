import os
_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False

ADMINS = frozenset(['steven@pequeno.in'])
SECRET_KEY = 'REPLACE ME'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')
DATABASE_CONNECT_OPTIONS = {}

THREADS_PER_PAGE = 8

WTF_CSRF_ENABLED = True
WTF_CSRF_SECRET_KEY = "somethingimpossibletoguess"

RECAPTCHA_USE_SSL = False
RECAPTCHA_PUBLIC_KEY = '6Lc2AQwTAAAAAGeyc50GjJuSiRD6NN_ZtKFjnjln'
RECAPTCHA_PRIVATE_KEY = '6Lc2AQwTAAAAAK86pWjPXmbqZhnx9AgcQEV9TpvK'
RECAPTCHA_OPTIONS = {'theme': 'white'}