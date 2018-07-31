import multiprocessing
from os import environ

bind = '0.0.0.0:'+environ.get('PORT','8000')
workers = multiprocessing.cpu_count() * 2 + 1
#accesslog = '/var/log/gunicorn/gunicorn-access.log'
#errorlog = '/var/log/gunicorn/gunicorn-error.log'
#loglevel = 'info'