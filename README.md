# schnitz3l
In Haft , da jagen wir vegane schnitz3l

## Table of Contents
  - [Running the app locally](#running-the-app-locally)
    - [Prerequisites](#prerequisites)
    - [Start virtual environment](#start-virtual-environment)
    - [Using Django's `manage.py`](#using-djangos-managepy)
      - [Before the first run](#before-the-first-run)
      - [Run the application](#run-the-application)
  - [The `.env` File](#the-env-file)
  - [Architecture overview](#architecture-overview)
  - [Code documentation](#code-documentation)

## Running the app locally

### Prerequisites
You need to have
  * the django secret key for running the app (best in the `.env` File)
  * python3.8 installed 
  * if your current python version is newer, you might also install `sudo apt-get install python3.10-venv`

### Start virtual environment

1. Create the virtual environment with `python3.10 -m venv venv`
2. Activate it, using `source venv/bin/activate` in the project folder
3. Verify you are in the venv with `which python`. This should point to somewhere within this project's venv.
4. Follow the steps in the next subsection to run the app in the virtual environment.
5. Later, when you want to leave the virtual environment, type `deactivate`.


### Using Django's `manage.py

#### Before the first run

+ In the project directory, where the file `requirements.txt` lives, run 
    `pip install -r requirements.txt`

+ before the first run, create the database. In project-parent/webapp run
    * `python manage.py migrate`

#### Run the application

+ start the server with
    `python manage.py runserver`

+ Stop the server with `ctrl` + `c`

+ when code is updated the server will restart automatically 


## The `.env` File

The environment file holds all configuration for the application. This file is not provided by this repo. You need to get or create it by yourself.

```
DOMAIN=nebu.uber.space
ADMIN_EMAIL=johanneshoess@posteo.de
ROOT_URL=nebu.uber.space/
DJANGO_SECRET_KEY='django-super-secret-key'
DEBUG=True
DATABASE=SQLite
DATABASE_NAME='schnitz3l'
DATABASE_USERNAME='myuser'
DATABASE_PASSWORD='mypass'
DATABASE_HOST='localhost'
DATABASE_PORT=''
```
#### DJANGO_SECRET_KEY
A secret key for a particular Django installation. This is used to provide cryptographic signing, and should be set to a unique, unpredictable value.
As written in the [django docs](https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-SECRET_KEY).

#### DEBUG
In debug mode errors will be displayed in the application which could lead to security vulnerability's. In Production set DEBUG to `False`.

#### DATABASE
This can be `SQLite` (created by django on migrate) or `Postgres` if existent. In case of Postgres you need to provide database name, credentials, host and port.

## Architecture overview
... to be written

## Code documentation
... to be written