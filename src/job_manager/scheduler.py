import logging
from datetime import datetime, timedelta
import crawler
from apscheduler.schedulers.background import BackgroundScheduler

schedr = BackgroundScheduler()


def start_scheduler():
    logging.info("Starting Scheduler")  # TODO: why logging not working?
    print("------****------Starting Scheduler------****------")
    schedr.add_jobstore('mongodb', collection='active_jobs', database='swacheckin')
    try:
        schedr.start()
    except (KeyboardInterrupt, SystemExit):
        pass


def schedule_job(entry):
    print("Creating job, stored into db and schedule to trigger by date.{0}".format(entry))
    alarm_time = datetime.now() + timedelta(seconds=5)  # Testing
    print("Your job will run the job at: {0}".format(alarm_time))
    schedr.add_job(crawler.crawl_checkin_page, 'date', run_date=alarm_time, args=[entry['confirmationNumber'],entry['firstName'],entry['lastName'],entry['phoneNumber']])

