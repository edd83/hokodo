## Setup


Activate the environment

```. venv/bin/activate```


Get env variable for production

```export APP_ENV=Production```


Install dependencies

```pip install flask```

```pip install requests```

```pip install pipenv```

```pipenv install --system --skip-lock```

```pip install gunicorn[gevent]```



## Run



You should be in /venv to run this


```gunicorn --worker-class gevent --workers 8 --bind 0.0.0.0:5000 wsgi:app --max-requests 10000 --timeout 5 --keep-alive 5 --log-level info```



## Tests



```pytest -v test_app.py```


Postman collection included, import in postman to be able to run it



## Challenges



Did some python parsing 5 years ago (couple of lines)


Tested Django, but feel easier with Flask on entry level




## To include with more time



More tests


DB to populate with hokodo books


Other endpoints to add books, modify books, delete books


Docker
