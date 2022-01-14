# rindus_user
###### A Django CRUD App with PostgreSQL for a Rindus programming task

## Pre-requisites
 - Python3.8
 - Django4.0
 - PostgreSQL
 - pip `sudo apt-get install python3-pip`
 - virtualenv (venv) `pip3 install virtualenv`
 - *Note*: this guide is based on Linux (Ubuntu)

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
 - Edit this file `vim /etc/postgresql/14/main/postgresql.conf`
   - The `14` folder name could change. It is the version of your Postgres
   - *Note*: use `vim` or any other editor of your choice
 - Search the port line and change it `port = 5431`
 - Restart postgreSQL `service postgresql restart`

## How to run the app
 - from `rindus_user` local folder, run `python manage.py migrate`
 - `python manage.py runserver`
 - create a superuser `python manage.py createsuperuser`
   - Follow the steps (username, email, password)

#### Google authentication
 - Open your web browser and go to http://127.0.0.1:8000/admin/
 - Log in using your superuser credentials
 - Now, under Sites button, click +Add
   - put *127.0.0.1:8000* as both the Domain name and Display name
   - SAVE
   - check the ID from this new site created and update the `SITE_ID` from `settings.py`
   - for example: `SITE_ID = 4`
 - Then, under Social Applications, click +Add and fill in the details as follows:
   - Provider: Google
   - Name: Rindus User
   - Client id: XXXX
   - Secret key: XXXX
   - *Key: (keep it empty)*
   - Sites: 127.0.0.1:8000 (under chosen sites)
   - SAVE
 - Log Out

#### Possible error
If you get an error like this:
`SocialApp matching query does not exist at http://127.0.0.1:8000/accounts/google/login/`
  
The `SITE_ID` in `settings.py` does not match with the site_id created from /admin. Check it here:
http://127.0.0.1:8000/admin/sites/site/
and update it.

#### Create a staff_crud group
To manage administrators permissions, we will create a group for them.
 - Go to /admin
 - Log in with your superuser
 - Go to http://127.0.0.1:8000/admin/auth/group/add/
   - Name: `staff_crud`
   - Permissions: Select the `user_app` related (four of them: CRUD)
     - add, change, delete and view
     - click on Choose button
     - they must be under `Chosen permissions`
   - SAVE

## How to use the app

 - Go to http://127.0.0.1:8000/
 - Click on Login With Google
 - Click on Continue button
 - Select a Google account to Sign in
   - you would see a Welcome page with your Google account name
 - Click on Go user crud page
 - Create, Read, Update or Delete users

## PENDING

1. IBAN data validation
2. Test environment using docker-compose to run the test task and doc
3. Documentation maintenance

#### EXTRAS
 - postgreSQL running on a docker container
 - The `SITE_ID` from `settings.py`, could be automated?
 - The `Social applications` record, could be automated?
 - Keys from `.env` file?
 - The group manually created, could be a migration?
 - The group manually assigned to new users, could be automated?