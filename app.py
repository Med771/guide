import json

from flask import Flask, render_template, request

from algorithm.dijkstra_algorithm import dijkstra

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("form.html")


@app.route("/answer", methods=['POST'])
def answer():
    values = ("start", "end", "time", "cafes", "sights", "museums", "theaters", "parks")

    start, finish, path_time = (request.form[value] for value in values[:3])
    cafes, sights, museums, theaters, parks = (request.form.get(value) for value in values[3:])

    time_ = int(path_time[:2]) * 3600 + int(path_time[3:]) * 60

    answer, path = dijkstra(start=start, finish=finish, time_path=int(time_))

    with open("data\\points_name.json", "r", encoding="utf-8") as f:
        name_points = json.load(f)

    res_path = [name_points[v[1]] + v[1] for v in path[1:]]

    print(*res_path, sep="\n")

    return render_template("answer.html", ans=answer)


if __name__ == '__main__':
    app.run()
