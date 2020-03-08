# -*- coding:utf-8 -*-
# List of modules to import when the Celery worker starts.
imports = ('test_celery.tasks',

           )

## Broker settings.
broker_url = 'redis://127.0.0.1:6379'

## Using the database to store task state and results.
result_backend = 'redis://127.0.0.1:6379'

task_annotations = {
    'tasks.add': {'rate_limit': '10/m'}
}

task_routes = {
    'tasks.add': 'low-priority',
}

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'Europe/Oslo'
enable_utc = True