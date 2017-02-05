## To run server
1. first install mysql,pip,python,django,mysqlclient
2. create a db in mysql
3. `cd almabase`
4. `python manage.py migrate`
5. restore dump added in pics to this db
6. `python manage.py runserver 0.0.0.0:8000`
7. go to http://127.0.0.1:8000

## Steps done to reach here

1. `install python`
2. `install pip`
3. `install django`
4. `pip install virtualenvwrapper-win`
5. `mkvirtualenv myproject`
6. `mkdir projectname`
7. `cd projectname`
8. `django-admin startproject almabase`
9. `pip install django mysqlclient`
10. `python manage.py makemigrations`
11. `python manage.py createsuperuser`
12. `python manage.py runserver`
13. create models.py from existing database
    by `python manage.py inspectdb > models.py`
14. `python manage.py createapp games`
    and add games' to INSTALLED_APPS in settings.py
15. `python manage.py makemigrations games`
16. `python manage.py sqlmigrate games 0001`
17. `python manage.py migrate`
18. import/restore dumb to your table
19. Edit views.py in games app folder
20. create templates folder in which add index.html
    to show list passed by index method in views.py
21. Write search method on game model
22. Write html for all filters  
