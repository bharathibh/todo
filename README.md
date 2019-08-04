# TODO - Django App

Simple Django TODO App

## Installation

Create new virtualenv for Python 3

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Django.

```bash
pip install Django
```

## Usage

```python
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

```
Used basic Class Based Views for CRUD operations

Items which are deleted will be marked as `is_deleted` `True` in DB.

The project uses SQLite as Database, so no external connection was needed while installation

The Django Admin can view all the created entries via default Django Admin Interface at [Django Admin](http://localhost:8000/admin)

Where the Admin export the selected entries as CSV in the dropdown

![[Screenshot](https://ibb.co/NKgCvRR)](https://i.ibb.co/Fzk3rpp/Screenshot-2019-08-04-at-8-04-04-PM.png)


## License
[MIT](https://choosealicense.com/licenses/mit/)