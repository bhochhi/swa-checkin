from flask import Flask, render_template, request
from job_manager import scheduler, checkin_store as dm
import logging
import os

# TODO: make is configurable
logging.getLogger().setLevel(logging.INFO)

app = Flask(__name__)
logging.info("Initialing application")

MONGO_URL = os.environ.get('MONGODB_URL',  default="mongodb://localhost:27017/swa-checkins")
logging.info("MONGO URL: %s", MONGO_URL)

logging.info('Testing config vars==> %s', os.environ.get('TEST_KEY'))


# TODO: export to routes file
@app.route("/")
def signup():
    return render_template('checkin.html')


@app.route('/checkin', methods=['POST'])
def checkin():
    # read the posted values from the UI
    _confirmationNumber = request.form.get('confirmationNumber')
    _fName = request.form.get('firstName')
    _lName = request.form.get('lastName')
    _phoneNumber = request.form.get('phoneNumber')
    _email = request.form.get('email')
    _date = request.form.get('scheduleDate')
    logging.info(
        "New request:==> {0}, {1}, {2}, {3}, {4}, {5}".format(_confirmationNumber, _fName, _lName, _email, _phoneNumber,
                                                              _date))
    # TODO: validate the inputs/request

    if dm.create_new_entry(request.form):
        scheduler.schedule_job(request.form)
        return '<span>You are all set!! Scheduled to checkin at ' + str(_date) + '</span>'
    return '<span>Something went wrong</span>'


if not scheduler.is_scheduler_running():
    scheduler.start_scheduler()

if __name__ == "__main__":
    app.run(debug=False, use_reloader=False)
