pip3 install -r requirements.txt
gunicorn --workers 1 --log-file - app:app
