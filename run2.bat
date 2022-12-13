clear
cd microfe
## initiate the database
python manage.py migrate
## check it works
python manage.py runserver 7080  --settings=microfe_main
