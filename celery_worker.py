import os
from celery import Celery
broker = os.environ['REDIS_URL']
backend = os.environ['REDIS_URL']
celery_name = os.environ['CELERY_NAME']

celery = Celery(celery_name, broker=broker,
                backend=backend)

@celery.task(name='celery_worker.test', bind=True)
def test(self, data):
    task_id = self.request.id
    return '{} test OK.'.format(task_id)
