Census API 
===================

### Installation

python manage.py makemigrations census

python manage.py sqlmigrate census 000X

python manage.py migrate

Use After Install

python manage.py runserver 

Access Admin /admin and Enter CensusAPI key, Select State and Housing Vairables to Data base

Use below to import pending views

python manage.py censuscall 
