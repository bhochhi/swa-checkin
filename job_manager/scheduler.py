import logging
# import datetime as dt
import os
from datetime import datetime, timedelta

from apscheduler.schedulers.background import BackgroundScheduler
from swa_review_client import fetch

schedr = BackgroundScheduler()

MONGO_URL = os.environ.get('MONGODB_URL', default="mongodb://localhost:27017/swa-checkins")


def is_scheduler_running():
    schedr.running


def start_scheduler():
    logging.info("Starting Scheduler")
    logging.info("------****------Starting Scheduler------****------")
    schedr.add_jobstore('mongodb', collection='active_jobs', database='swa-checkins', host=MONGO_URL)
    try:
        schedr.start()
    except (KeyboardInterrupt, SystemExit):
        pass


def schedule_job(entry):
    logging.info("Creating job, stored into db and schedule to trigger by date.{0}".format(entry))
    alarm_time = datetime.strptime(entry['scheduleDate'], "%Y-%m-%dT%H:%M:%S%z") + timedelta(seconds=10)
    # alarm_time = datetime.parse(entry['scheduleDate']) + timedelta(seconds=10)  # Testing
    # date_time_requested = datetime.datetime.strptime(entry['scheduleDate'], '%m/%d/%Y %H:%M ')

    # alarm_time = date_time_requested + timedelta(seconds=10)  # Testing

    logging.info("Your job will run the job at: {0}".format(alarm_time))
    schedr.add_job(fetch,
                   'date',
                   run_date=alarm_time,
                   args=[entry['confirmationNumber'], entry['firstName'], entry['lastName']])
