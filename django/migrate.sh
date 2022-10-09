#!/bin/bash

SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-"admin@admin.com"}
cd /app/

python manage.py collectstatic 
python manage.py migrate
python manage.py createsuperuser --email $SUPERUSER_EMAIL || true