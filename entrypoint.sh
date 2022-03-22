#!/bin/sh

echo "== Starting Django app: $INSTALL_DIR: $DJANGO_SETTINGS_MODULE"
echo "Waiting for mysql..."
while ! nc -z ${MY_DB_HOST:-db} ${MY_DB_PORT:-3306}; do
  sleep 0.1
done
echo "MySQL started"

cd $INSTALL_DIR
python3 manage.py migrate


echo "Starting Gunicorn ......."
gunicorn -v
gunicorn api.wsgi:application --bind=0.0.0.0:8000 --log-level='debug' --capture-output

#python3 -m http.server 8000
