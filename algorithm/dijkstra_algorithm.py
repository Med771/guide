import json

from collections import deque

with open("data\\matrix_time_minimal_graph.json", "r") as f:
    matrix_distance = json.load(f)

with open("data\\time_graph.json", "r") as file:
    time_graph = json.load(file)


def dijkstra(start, finish, time_path):
    queue = deque([(0, start, [(0, 0)])])

    answer, result_path = 0, []

    while queue:
        dist, start, path = queue.popleft()

        if matrix_distance[start][finish] > time_path - dist:
            continue

        if len(path) > 25:
            continue

        for weight, long in time_graph[start].items():
            if (weight, start) in path and len(time_graph[start]) != 1:
                continue

            if (start, weight) in path and len(time_graph[start]) != 1:
                continue

            distance = dist + long

            if distance > time_path:
                continue

            if weight == finish:
                if answer < distance:
                    answer = distance
                    result_path = path.copy() + [(start, weight)]
            else:
                queue.append((distance, weight, path + [(start, weight)]))

    return result_path
