# Django Rest Framework GenericAPIView & Mixins
A simple example for Django Rest Framework using GenericAPIViews and Mixins.

## Used DRF Conventions
- ModelSerializer
- GenericAPIView
- Permissions
- Pagination
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