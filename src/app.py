from flask import Flask, render_template, request
import data_manager as dm
from job_manager import scheduler


app = Flask(__name__)

class Config(object):
    JOBS = [
        {
            'id': 'job1',
            'func': 'app:job1',
            'args': (1, 2),
            'trigger': 'interval',
            'seconds': 10
        }
    ]

    SCHEDULER_API_ENABLED = True

def job1(a, b):
    print(str(a) + ' ' + str(b))

def alarm(message="default message"):
    print('Alarm! This alarm was scheduled at {0}.'.format(message))



@app.route("/")
def signup():
    return render_template('checkin.html')


@app.route('/checkin', methods=['POST'])
def checkin():
    # read the posted values from the UI
    # form = request.form.convert_to_dict()
    _confirmationNumber = request.form.get('confirmationNumber')
    _fName = request.form.get('firstName')
    _lName = request.form.get('lastName')
    _phoneNumber = request.form.get('phoneNUmber')
    _email = request.form.get('email')
    _date = request.form.get('scheduleDate')
    print("Entry:==> {0}, {1}, {2}, {3}, {4}, {5}".format(_confirmationNumber, _fName, _lName, _email, _phoneNumber,
                                                          _date))
    print(request.form)
    if dm.create_new_entry(request.form):
        # TODO create job and scheduled.
        # TODO create job and scheduled.
        # scheduler.start_scheduler()
        scheduler.schedule_job(request.form)
        return '<span>You are all set!! Scheduled to checkin at ' + _date + '</span>'
    return '<span>Something went wrong</span>'

if __name__ == "__main__":

    #
    scheduler.start_scheduler()
    app.run(debug=True)
    # checkintest()
