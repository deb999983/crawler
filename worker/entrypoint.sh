#!/bin/sh

echo "== Starting Django app: $INSTALL_DIR: $DJANGO_SETTINGS_MODULE"
echo "Waiting for mysql..."
while ! nc -z ${MY_DB_HOST:-db} ${MY_DB_PORT:-3306}; do
  sleep 0.1
done
echo "MySQL started"

echo "Starting worker..."
python worker/worker.py
