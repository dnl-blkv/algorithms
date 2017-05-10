# O(v^2) implementation of Dijkstra's algorithm
import sys


def dijkstra(g, s):
    q = set(g.keys())
    dist = [sys.maxsize] * len(g)
    prev = [None] * len(g)
    dist[s] = 0

    while q:
        u = min(q, key=lambda e: dist[e])  # Can use fibonacci heap here for faster access to min
        q.remove(u)

        for v in g[u]:
            alt = dist[u] + g[u][v]

            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u

    return dist, prev

# test
graph = {
    0: {1: 100, 2: 5},
    1: {3: 1, 4: 7},
    2: {3: 1, 4: 1},
    3: {4: 20, 2: 1, 1: 6},
    4: {},
}
print(dijkstra(graph, 0))

