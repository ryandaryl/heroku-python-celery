# Minimal Python Celery web/worker queue
This web application includes a Flask web interface and Celery worker.

The web process is set up for long-polling: a GET request to `/test` returns a task ID, which can be used to poll for results at `/tasks/<task_id>`.
The code is a port to Celery of my earlier [heroku-python-worker](https://github.com/ryandaryl/heroku-python-worker).

I've added app.json and this readme so you can:

## Deploy to Heroku
By clicking the button below.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
