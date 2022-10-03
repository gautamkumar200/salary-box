
from time import sleep

from celery import shared_task
from celery_app import celery_app


@celery_app.task(queue="gautam_task_queue")
def call_celery_task():
    for i in range(10):
        print("executing celery task ....")
        sleep(2)
