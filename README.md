# rindus_user
###### A Django CRUD App with PostgreSQL for a Rindus programming task

## Pre-requisites
 - Python3.8
 - Django4.0
 - PostgreSQL
 - virtualenv (venv)
 - Note: this guide is based on Linux (Ubuntu)

## How to set up
 1. clone the project: `git clone git@github.com:Quitiweb/rindus_user.git`
 2. go to your `rindus_user` local folder `cd rindus_user`
 3. create a new virtual environment: `python -m venv ~/venvs/rindus_user`
 4. `source ~/venvs/rindus_user/bin/activate`
 5. install the packages from requirements.txt -> `pip install -r requirements.txt`

## DataBase PostgreSQL

 - Install PostgreSQL: `sudo apt install postgresql`
 - Assign a password to `postgres` user: `passwd postgres`
 - Log in to that user: `su postgres`

#### Create a DataBase, a user and assign a password
```
$ createdb rindus_db
$ createuser rafael
$ psql
=# ALTER USER rafael WITH PASSWORD 'pass4r1ndus';
```

#### Change PostgreSQL default port
 - Edit `/etc/postgresql/14/main/postgresql.conf`
 - `port = 5431`
 - Restart postgreSQL `service postgresql restart`

## How to run the app
 1. from `rindus_user` local folder, run `python manage.py migrate`
 2. `python manage.py runserver`

## PENDING

1. IBAN data validation
2. Write documentation on how to set up, run and use your implementation
3. Test environment using docker-compose to run the test task and doc

 - EXTRA: The group manually created, maybe could be a migration
 - EXTRA: postgreSQL running on a docker container
