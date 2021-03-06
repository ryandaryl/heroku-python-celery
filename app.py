import os
import logging
from flask import Flask, request, jsonify
from celery import Celery

broker = os.environ['REDIS_URL']
backend = os.environ['REDIS_URL']
name = os.environ.get('CELERY_NAME', 'default_name')

app = Flask(__name__)

celery = Celery(name, broker=broker, backend=backend)

@app.route('/tasks/<task_id>')
def check_task(task_id):
    task = celery.AsyncResult(task_id)

    if task.state == 'FAILURE':
        result = None
        error = str(task.result)
    else:
        result = task.result
        error = None

    response = {
        'id': task_id,
        'state': task.state,
        'result': result,
        'error': error,
    }
    return jsonify(response)

@app.route('/test')
def handle_job():
    task = celery.send_task('celery_worker.test', args=[request.form])
    response = check_task(task.id)
    return response

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 80))
    app.run(host='0.0.0.0', port=port)
