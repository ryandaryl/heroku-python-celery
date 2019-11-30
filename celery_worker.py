import os
from celery import Celery
from celery.signals import worker_process_init
from billiard import current_process
broker = os.environ['REDIS_URL']
backend = os.environ['REDIS_URL']
name = os.environ.get('CELERY_NAME', 'default_name')

celery = Celery(name, broker=broker,
                backend=backend)

my_global_var = None

@worker_process_init.connect()
def on_worker_init(**_):
    import datetime
    global my_global_var
    my_global_var = datetime.datetime.now()

@celery.task(name='celery_worker.test', bind=True)
def test(self, data):
    current_process_index = current_process().index
    task_id = self.request.id
    return '{}: {} test OK.'.format(current_process_index, task_id)
