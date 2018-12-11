from flask import Flask, render_template, json, request

app = Flask(__name__)


# @app.route("/")
# def main():
#     return render_template('index.html')

@app.route("/")
def signup():
    return render_template('checkin.html')


@app.route('/checkin', methods=['POST'])
def checkin():
    # read the posted values from the UI
    _confirmationNumber = request.form['confirmationNumber']
    _fName = request.form['firstName']
    _fLast = request.form['lastName']
    print(_confirmationNumber)
    print(_fName)
    print(_fLast)
    return json.dumps({'html': '<span>All fields good !!</span>'})


if __name__ == "__main__":
    app.run()
