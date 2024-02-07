#!/bin/bash

echo "API SERVER RUN"
python manage.py migrate # Apply migrations

# Load data from fixtures
python manage.py loaddata fixtures/accounts.json
python manage.py loaddata fixtures/shop.json

python manage.py collectstatic
# Start the Gunicorn server
gunicorn --config gunicorn_config.py ecommerce_innovation.wsgi:application
