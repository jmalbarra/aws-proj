from flask import Flask
import datetime

app = Flask(__name__)

@app.route("/ping)")
def ping():
    return "pong"


@app.route("/")
def horaActual():
    return str(datetime.datetime.now())

if __name__ == '__main__':
    app.run(debug=True)