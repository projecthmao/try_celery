from celery import Celery
from celery.schedules import crontab
import datetime

kl = 1

app = Celery('tasks', broker='redis://localhost:6379/0')
app.conf.beat_schedule = {
    'update_data-every-single-minute': {
        'task': 'tasks.test',
        'schedule': crontab(),  # change to `crontab(minute=0, hour=0)` if you want it to run daily at midnight
    },
}


@app.task
def test():
    global kl
    print(datetime.datetime.now())
    kl +=1
    return kl



test()


        # 'task': 'data.tasks.update_data',
