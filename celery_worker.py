import os
from celery import Celery
broker = os.environ['REDIS_URL']
backend = os.environ['REDIS_URL']
name = os.environ.get('CELERY_NAME', 'default_name')

celery = Celery(name, broker=broker,
                backend=backend)

@celery.task(name='celery_worker.test', bind=True)
def test(self, data):
    task_id = self.request.id
    return '{} test OK.'.format(task_id)
