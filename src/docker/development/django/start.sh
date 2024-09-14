#!/bin/bash 


set -o errexit 


set -o nounset 


python /home/movio/app/manage.py makemigrations --no-input 
python /home/movio/app/manage.py migrate --no-input 
python /home/movio/app/manage.py collectstatic --no-input  --clear 

exec /home/movio/app/manage.py runserver 0.0.0.0:8000
