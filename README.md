# DRF_project_samples
Projects for understanding Django Rest Framework

---
## Project Requirements

- Python 3.9.10
  
### Used Packages in all Projects
- Django 3.2
- djangorestframework 3.13
- requests 2.27.1 (for http reqeust actions)
- pillow 9.0.1 (imaging library)
---

## set python venv

Use python virtual environment.

```bash
$ python3.9 -m venv .venv

$ source .venv/bin/activate
```
---

## Managing Django

### install packages

```bash
$ python -m pip install --upgrade pip

$ pip install Django==3.2
$ pip install djangorestframework==3.13
```

### start django project
```bash
$ mkdir tutorial
$ cd tutorial

$ django-admin startproject <PROJECT_NAME> .
$ python manage.py startapp <APP_NAME>
```

### use admin with default database(sqlite)
```bash
$ python manage.py migrate
$ python manage.py createsuperuser
```

