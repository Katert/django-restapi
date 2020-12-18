release: python restapi/manage.py makemigrations
release: python restapi/manage.py migrate

web: gunicorn restapi.wsgi
