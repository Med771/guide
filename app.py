from flask import Flask, render_template, request
from algorithm.building_path import building_path
from time import time

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route("/answer", methods=['POST'])
def answer():
    values = ("start", "end", "time", "cafes", "sights", "museums", "theaters", "parks")

    start, end, path_time = (request.form[value] for value in values[:3])
    cafes, sights, museums, theaters, parks = (request.form.get(value) for value in values[3:])

    print(start, end)

    time_ = int(path_time[:2]) * 3600 + int(path_time[3:]) * 60

    start_time = time()

    answer_path = building_path(start_point=start, end_point=end, time_path=time_)

    end_time = time()

    print(end_time - start_time)

    return render_template("answer.html", total_path=answer_path)

if __name__ == '__main__':
    app.run()
