# recipe-app-api



docker build . --> creates the image
docker-compose build -> also creates the image using docker-compose


in dockerfile we set ARG DEV=false and this is only for default and if we do not specify something else. insid ethe docker-compose file, we set ARG DEV=true which overwrites it


we are excluding some files from linting inside the .flake8 file --> docker-compose run --rm app sh -c "flake8"

docker-compose run --rm app sh -c "django-admin startproject app ." --> creating a new project called app inside our current directory

docker-compose up --> starts our services (go to http://127.0.0.1:8000/)
docker-compose run --rm app sh -c "python manage.py test" --> tests our code

### github actions
Create a new file in your repository called ".github/workflows/checks.yml" and add this code inside it:
yaml
name: CI
on: [push]
jobs:
build:
runs-on: ubuntu-latest
steps:
- uses: actions/checkout@v2
- name: Set up Python 3.x
uses: actions/setup-python@v2
with:
python-version: '3.x'
- name: Install dependencies
run: |
pip install -r requirements.txt
