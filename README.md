# DRF_project_samples
A project for Django Rest Framework

---

## Project Requirements

- Python 3.9.10
  
### Used Packages
- Django 3.2
- djangorestframework 3.13
- requests 2.27.1
---

## 1. How to start Django Rest Framework project.

### set python venv

Use python virtual environment.

```bash
$ python3.9 -m venv .venv

$ source .venv/bin/activate
```

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