# lincassable-platform

cp env.dist env

source .venv/bin/activate
cd lincassable
python manage.py runserver

### With pipenv

pipenv install
pipenv shell
python manage.py runserver

### Run tests

createdb lincassable_test
pytest