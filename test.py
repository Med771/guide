import time

from algorithm.dijkstra_algorithm import dijkstra

S, F = input("S and F: ").split()
time_ = int(input("time: ")) * 60

start = time.time()

ans, res = dijkstra(S, F, time_)

print(*res)

if res:
    print(f"ans = {ans}")
else:
    print("No path found")

total = time.time() - start
path = ""

for v in res:
    path += f"{v[0]} -> {v[1]} |"

print(f"sec: {total}")

with open("log/log.txt", "a") as f:
    f.write(f"{S} -> {F} {ans} {total}\n")
    f.write(f"{path}\n")
