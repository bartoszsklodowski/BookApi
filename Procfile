release: python manage.py makemigrations --no-input
release: python manage.py migrate
release: python manage.py loaddata fixtures.json

web: gunicorn Books.wsgi