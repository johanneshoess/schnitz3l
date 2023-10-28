supervisorctl status
~/schnitz3l/venv/bin/python manage.py collectstatic
~/schnitz3l/venv/bin/python manage.py migrate
supervisorctl restart schnitz3l
