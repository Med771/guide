import json

from collections import deque


with open("data\\matrix_distance_points.json", "r") as f:
    matrix_distance = json.load(f)

with open("data\\path_time.json", "r") as file:
    graph = json.load(file)


def dijkstra(start, finish, time_path):
    queue = deque([(0, start, [(0, 0)])])

    answer, result_path = 0, []

    while queue:
        dist, start, path = queue.popleft()

        if matrix_distance[start][finish] > time_path - dist:
            continue

        for weight, long in graph[start].items():
            if (start, weight) in path or ((weight, start) in path and len(graph[weight]) != 1):
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

    return answer, result_path
