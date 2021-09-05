# BookApi App
> Manage and view books fetch from googleapi.
> Live demo [_here_](https://google-book-api-skl.herokuapp.com/). <!-- If you have the project hosted somewhere, include the link here. -->

Login details admin: `admin`/`Adminadmin123`

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Setup](#setup)
* [Usage](#usage)
* [Contact](#contact)


## General Information
- Application was created to learn how to handle data from API.
- General purpose is to download data from googleapi and save to database creating book objects.
- You can use HTTP methods (GET, POST, PUT, DELETE) on book objects and post data to update database.
- I made this project because I want to develop my skills in making Python and Django Rest Framework projects.


## Technologies Used
- Python - version 3.9
- Django - version 3.2


## Features
List the ready features here:
- Filter by published_date and authors for Book model.
- Pagination.
- Ordering by published_date.


## Setup

What are the project requirements/dependencies? Where are they listed? A requirements.txt or a Pipfile.lock file perhaps? Where is it located?

Proceed to describe how to install / setup one's local environment / get started with the project.

#### The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/bartoszsklodowski/BookApi.git
$ cd BookApi
```

#### Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

#### Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

#### Database

To work in local environment you must uncomment DATABASE variable for SQLite3 and comment for Heroku deployment.

#### Migrate database

```sh
$ python manage.py makemigrations
$ python manage.py migrate
```

#### Create superuser

Create a local admin user by entering the following command:

`python manage.py createsuperuser`


#### Start the app

`python manage.py runserver 0.0.0.0:8000`

#### Add initial data

You can add initial data either by going to the url the app is running on locally and adding `/admin` to the url.

Add some categories and you should be all set.

Or by entering 

`python manage.py loaddata fixtures.json`

[comment]: <> (## Tests)

[comment]: <> (To run the tests, `cd` into the directory where `manage.py` is:)

[comment]: <> (```sh)

[comment]: <> (&#40;env&#41;$ python pytest)

[comment]: <> (```)

## Usage

* Update database with books which title contain given word(POST method) => `/db/?q="war"`
* List of all books => `/books/`
* Detail view of specific book => `/books/<id>/`
* Filter books by published_date => `/books/?published_date=1995`
* Filter books by authors => `/books/?authors="Rowling"`
* Set order ascending or descending by published_date => `/books/?ordering=(-)published_date`

You can join filters and ordering.

## Contact
Created by [@bartoszsklodowski](https://linkedin.com/in/bartosz-skłodowski) - feel free to contact me!