web: gunicorn app:app --workers 2 --bind 0.0.0.0:${PORT:-80} --log-file - --log-level=debug --access-logfile -
worker: celery --app="celery_worker" --loglevel=info --concurrency=1 worker
