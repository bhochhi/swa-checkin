import logging
from datetime import datetime, timedelta
from flask import json, current_app, jsonify

from apscheduler.schedulers.background import BackgroundScheduler

schedr = BackgroundScheduler()

def start_scheduler():

    # schedr.configure({'apscheduler.daemonic': False})
    logging.info("Starting Scheduler")
    print("------****------Starting Scheduler------****------")
    # schedr.init_app(current_app)
    schedr.add_jobstore('mongodb', collection='active_jobs', database='swacheckin')
    try:
        schedr.start()
    except (KeyboardInterrupt, SystemExit):
        pass


def schedule_job(entry):
    # TODO: make sure scheduler is started
    print("Creating job, storing into db and schedule to trigger by date.{0}".format(entry))

    alarm_time = datetime.now() + timedelta(seconds=5)
    print("will run the job at: {0}".format(alarm_time))
    schedr.add_job(alarm, 'date', run_date=alarm_time, args=[datetime.now(), 'Hello world', alarm_time, entry])
    print(schedr.print_jobs())



def alarm(time, message="default message", run_date="", entry={}):
    print('Alarm! This alarm was scheduled at {0}. with message {1} executed at {2} for entry: {3}'.format(time, message, run_date,entry))
