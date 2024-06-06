import json

from time import time

from algorithm.dijkstra_algorithm import dijkstra


def create_response_path(start: str, end: str, time_path: int) -> tuple[list[dict[str, str]], int]:
    answer_time, answer_path = dijkstra(start, end, time_path)

    response = []

    with open("data\\points_name.json", "r") as file:
        data = json.load(file)

    for value in answer_path:
        response.append({"text": data[value[1]]})

    return response, answer_time


if __name__ == "__main__":
    start = time()

    path, time_path = create_response_path("30", "1", 10800)

    print(path)
    print(time_path)
    print(time() - start)
