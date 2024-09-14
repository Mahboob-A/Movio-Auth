#!/bin/bash 


set -o errexit 


set -o nounset 


python /home/movio/app/manage.py makemigrations --no-input 
python /home/movio/app/manage.py migrate --no-input 
python /home/movio/app/manage.py collectstatic --no-input  --clear 

# port: 9005 
exec /usr/local/bin/gunicorn movio_auth_service.wsgi:application --bind 0.0.0.0:${DJANGO_APP_PORT} --chdir=/home/movio/app


