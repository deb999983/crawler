#!/bin/sh

echo "== Starting Django app: $INSTALL_DIR: $DJANGO_SETTINGS_MODULE"
echo "Waiting for postgres..."
while ! nc -z ${MY_DB_HOST:-wiki_store_db} ${MY_DB_PORT:-5432}; do
  sleep 0.1
done
echo "DB Ready ..."

echo "Starting worker..."
python src/worker.py
