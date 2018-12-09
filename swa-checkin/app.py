from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html')

@app.route("/static")
def static():
    return url_for('static', filename='style.css')

if __name__ == "__main__":
    app.run()

