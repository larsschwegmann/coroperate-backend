# coroperate-backend
You need Python 3.6 or newer.

## Set up
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
We're using `json`.

### GET

#### /requests/
Return a list of existing requests.

### POST

#### /requests/
Create a new request as well as the items demanded in that request.

#### /users/
Create a new user.

#### /token/
Obtain access and refresh JSON web token pair.

#### /token/refresh/
Return access token if refresh token is valid.
