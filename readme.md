# Loading Data with Django + Postgres
This is a small demo application built to compare different methods of 
loading data into Postgres from Django.

Start the containers: `docker-compose up -d` 
Run the migrations: `docker-compose exec web python manage.py migrate`
Enter the Python shell: `docker-compose exec web python manage.py shell`
Reset the database: `docker-compose exec web python manage.py flush --no-input`

## Method 1: Looping and Saving
docker-compose exec web python manage.py m1

## Method 2: Importing as Fixture
docker-compose exec web python manage.py m2 profiles1000

## Method 3: Using Django's `bulk_create()` Method
docker-compose exec web python manage.py m3

## Method 4: Using the `django-postgres-copy` Package
docker-compose exec web python manage.py m4
