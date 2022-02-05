# Django standard API example
A simple API using Django 

---

## Project Requirements

- Python 3.9.10

### Used Packages
- Django 3.2
- pillow 9.0.1 (imaging library)
---

## 1. Django Settings

### install packages

```bash
$ python -m pip install --upgrade pip

$ pip install Django==3.2
$ pip install pillow==9.0.1
```

### start django project
```bash
$ mkdir standard
$ cd standard

$ django-admin startproject onlinestore .

$ python manage.py migrate
$ python manage.py createsuperuser

$ python manage.py startapp products
```

### data migrations
```bash
$ python manage.py makemigrations
$ python manage.py migrate
```