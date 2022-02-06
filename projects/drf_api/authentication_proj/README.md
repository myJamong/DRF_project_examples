# Django Rest Framework Authentications
A simple example for Django Rest Framework using Authentications.

## Used DRF Conventions
- ModelSerializer
- Generic APIView  
- ViewSets & Routers
- Signals
- Django-REST-Auth
- Token Authentication
- Filtering
- Testing
---

## Project Requirements

- Python 3.9.10

### Used Packages
- Django 3.2
- djangorestframework 3.13 
- django-rest-auth 0.9.5
- requests 2.27.1
- django-allauth 0.48.0

---

## 1. Django Settings
### install packages

```bash
$ python -m pip install --upgrade pip

$ pip install Django==3.2
$ pip install djangorestframework==3.13
$ pip install django-rest-auth==0.9.5
$ pip install requests==2.27.1
```

### start django project
```bash
$ django-admin startproject ebooksapi .

$ python manage.py startapp ebooks
```

### data migrations
```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

### create admin user
```bash
$ python manage.py createsuperuser
```