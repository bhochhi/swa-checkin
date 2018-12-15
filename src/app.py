from flask import Flask, render_template, request
from job_manager import scheduler, checkin_store as dm

app = Flask(__name__)


@app.route("/")
def signup():
    return render_template('checkin.html')


@app.route('/checkin', methods=['POST'])
def checkin():
    # read the posted values from the UI
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
        scheduler.schedule_job(request.form)
        return '<span>You are all set!! Scheduled to checkin at ' + _date + '</span>'
    return '<span>Something went wrong</span>'


if __name__ == "__main__":
    scheduler.start_scheduler()
    app.run(debug=True)
