import logging
from datetime import datetime, timedelta
import os
from apscheduler.schedulers.background import BackgroundScheduler

import crawler

schedr = BackgroundScheduler()

MONGO_URL = os.environ.get('MONGODB_URL', default="mongodb://localhost:27017/swa-checkins")


def is_scheduler_running():
    schedr.running


def start_scheduler():
    logging.info("------****------Starting Scheduler------****------")
    schedr.add_jobstore('mongodb', collection='active_jobs', database='swa-checkins', host=MONGO_URL)
    try:
        schedr.start()
    except (KeyboardInterrupt, SystemExit):
        pass
    logging.info("------*^^*------Started Scheduler------*^^*------")


def schedule_job(entry):
    logging.info("Creating job, stored into db and schedule to trigger by date.{0}".format(entry))
    alarm_time = datetime.now() + timedelta(seconds=6)  # Testing
    # date_time_requested = datetime.datetime.strptime(entry['scheduleDate'], '%m/%d/%Y %H:%M ')

    # alarm_time = date_time_requested + timedelta(seconds=10)  # Testing

    logging.info("Your job will run the job at: {0}".format(alarm_time))
    schedr.add_job(crawler.crawl_checkin_page, 'date', run_date=alarm_time,
                   args=[entry['confirmationNumber'], entry['firstName'], entry['lastName'], entry['phoneNumber']])
    logging.info("Job Added")
