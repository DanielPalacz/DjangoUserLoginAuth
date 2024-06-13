# DjangoUserLoginAuth

```
python -m venv venv
source venv/bin/activate
pip install Django

django-admin startproject mysite
cd mysite
python manage.py startapp login
	register 'login' application

Developed 'login app':
	GET /login
	POST /logout
	GET /account
		- dashboard page

also in settings.py:
	LOGIN_REDIRECT_URL = "/account/"
	LOGOUT_REDIRECT_URL = "/"
	LOGIN_URL = "/login/"
	LOGOUT_URL = "/logout/"

```