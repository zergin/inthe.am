user = 'www-data'
group = 'www-data'
logfile = '/var/www/twweb/logs/gunicorn-status.log'
workers = 5
loglevel = 'debug'
bind = '127.0.0.1:8041'
timeout = 300
worker_class = 'eventlet'
