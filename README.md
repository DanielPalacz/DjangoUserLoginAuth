# DjangoUserLoginAuth
Usage of basic Django login / logout functionalities:
 - django.contrib.auth.views.LoginView
 - django.contrib.auth.views.LogoutView
 - django.contrib.auth.forms.UserCreationForm (register view/url)

```
python -m venv venv
source venv/bin/activate
pip install Django

django-admin startproject mysite
cd mysite
python manage.py startapp login
	register 'login' application

Developed html templates
 - login.html
 - user_logged_out.html
 - dashboard.html
 
settings.py:
	LOGIN_REDIRECT_URL = "/account/"
	LOGOUT_REDIRECT_URL = "/logged_out/"
	LOGIN_URL = "/login/"
	LOGOUT_URL = "/logout/"

Developed 'login' app endpoints:
	GET /login
	POST /logout
	GET /logged_out
	GET /account
		- dashboard page
```
