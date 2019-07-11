import os
import logging
from flask import Flask, request, jsonify, Blueprint
from celery import Celery

broker = os.environ['REDIS_URL']
backend = os.environ['REDIS_URL']
name = os.environ.get('CELERY_NAME', 'default_name')

app = Flask(__name__)

celery = Celery(name, broker=broker, backend=backend)

tasks_blueprint = Blueprint('tasks', __name__, url_prefix='/tasks')
@tasks_blueprint.route('/<task_id>', methods=['GET'])
def check_task(task_id):
    task = celery.AsyncResult(task_id)

    if task.state == 'FAILURE':
        result = None
        error = str(task.result)
    else:
        result = task.result
        error = None

    if isinstance(result, Exception):
        result = str(result)

    response = {
        'id': task_id,
        'state': task.state,
        'result': result,
        'error': error,
    }
    return jsonify(response)
app.register_blueprint(tasks_blueprint)

test_blueprint = Blueprint('parse', __name__, url_prefix='/test')
@test_blueprint.route('/', methods=['GET'])
def handle_job():
    task = celery.send_task('celery_worker.test', args=[request.form])
    response = check_task(task.id)
    return response
app.register_blueprint(test_blueprint)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 80))
    app.run(host='0.0.0.0', port=port)
