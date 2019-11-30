
# Minimal Python Celery web/worker queue

This web application includes a Flask web interface and Celery worker.

The web process is set up for long-polling: a GET request to `/test` returns a task ID, which can be used to poll for results at `/tasks/<task_id>`.

The code is a port to Celery of my earlier [heroku-python-worker](https://github.com/ryandaryl/heroku-python-worker).

## Install dependencies

Install Python 3.6

`python3.6 -m pip install -r requirements.txt`

`apt-get install redis-server`

## Set environment variables

`export REDIS_URL=redis://localhost`

OR build the Dockerfile to get an appropriate environment.

## Run the Redis server

`redis-server`

## Run web and worker processes using Honcho

`honcho start -c web=1,worker=1 -p 80`

You can use any port to host the web application. Just change the above to  `-p your_port_number`.

I've added app.json and this readme so you can:

## Deploy to Heroku
By clicking the button below.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
