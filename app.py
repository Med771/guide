import json

from flask import Flask, render_template, request

from algorithm.create_path import create_response_path

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route("/answer", methods=['POST'])
def answer():
    values = ("start", "end", "time", "cafes", "sights", "museums", "theaters", "parks")

    start, finish, path_time = (request.form[value] for value in values[:3])
    cafes, sights, museums, theaters, parks = (request.form.get(value) for value in values[3:])

    time_ = int(path_time[:2]) * 3600 + int(path_time[3:]) * 60

    response_path, response_time = create_response_path(start, finish, time_)

    return render_template("answer.html", items=response_path, total_time=response_time)


if __name__ == '__main__':
    app.run()
