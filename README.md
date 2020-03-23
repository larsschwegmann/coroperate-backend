# coroperate-backend
This is the back-end code for **coroperate**, an app that we developed for the [#WirVsVirus Hackathon](https://wirvsvirushackathon.org/) of the German government. Check out a description of our project on [Devpost](https://devpost.com/software/34_nachbarschaftshilfe_coroperate) or watch the pitch video on [YouTube](https://www.youtube.com/watch?v=vWjDtBLyH1g&feature=emb_logo).

This repo contains the back-end of the app, a REST API built with [django](https://www.djangoproject.com/) and [django REST framework](https://www.django-rest-framework.org/).

## Set up
You need Python 3.6 or newer.
Clone and enter the repo:
```
git clone git@github.com:larsschwegmann/coroperate-backend.git
cd coroperate-backend
```
Create and activate virtual environment:
```
python3 -m venv .venv
source .venv/bin/activate
```
Install requirements via pip:
```
pip install -r requirements.txt
```

## Running locally
Make sure you're in the outer `coroperate` directory. Then, run 
```
python manage.py runserver
```

## API
The following endpoints are provided:


```
/requests/
```
* GET: Return a list of existing requests.
* POST: Create a new request as well as the items demanded in that request.

```
/requests/<id>
```
* PUT: Accept the request with `<id>`

```
/users/
```
* POST: Create a new user

```
/token/
```
* POST: Obtain JSON web token pair.

```
/token/refresh/
```
* POST: Return access token if refresh token is valid.
