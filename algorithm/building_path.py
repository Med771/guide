import json

from algorithm.dijkstra_algorithm import dijkstra

with open("data\\points_position.json") as file:
    points_position = json.load(file)


def building_path(start_point, end_point, time_path):
    response = dijkstra(start_point, end_point, time_path)
    response[0] = (0, start_point)

    answer_path = [[float(points_position[value[1]]["lat"]), float(points_position[value[1]]["lon"])] for value in response]

    return answer_path
