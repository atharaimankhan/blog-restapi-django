# blog-restapi-django

### Install Docker

### Docker commands:
1. docker-compose up -d db
2. docker-compose exec db mysql -u root -p -e 'CREATE DATABASE `jinnah_tech_assignment_db` DEFAULT CHARACTER SET = `utf8mb4`'
3. docker-compose up -d app
4. docker-compose up -d phpmyadmin

### Three services will be running at a time:
1. db (MySQL database) rootpassword: root
2. app (the actuall django which deals with apis) URL: localhost:8000
3. phpmyadmin (phpmyadmin for the easy access to the database) URL: localhost:8081, username: root, password: root

### Django Admin:
docker-compose run app python manage.py createsuperuser
create admin user and go to localhost:8000/admin and login

### for Migrations Run:
docker-compose run app python manage.py makemigrations
docker-compose run app python manage.py migrate

### Run MySQL Scripts:
open phpmyadmin
goto SQL tab and run all the scripts available in mysql_scripts folder


