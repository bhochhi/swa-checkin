import time
import atexit
from apscheduler.schedulers.blocking import BlockingScheduler



def print_date_time():
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(func=print_date_time, trigger="interval", seconds=3)
    scheduler.start()

    # Shut down the scheduler when exiting the app
    atexit.register(lambda: scheduler.shutdown())


