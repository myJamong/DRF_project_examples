# Django Rest Framework class based view
A simple example for Django Rest Framework using class based views

## Used DRF Conventions
- ModelSerializer
- APIView(class based views)
- Serializer Validation
- Serializer Nested Relationships
---

## Project Requirements

- Python 3.9.10

### Used Packages
- Django 3.2
- djangorestframework 3.13
---

## 1. Django Settings
### install packages

```bash
$ python -m pip install --upgrade pip

$ pip install Django==3.2
$ pip install djangorestframework==3.13
```

### start django project
```bash
$ django-admin startproject newsapi .

$ python manage.py startapp news
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