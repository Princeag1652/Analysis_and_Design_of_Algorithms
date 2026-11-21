from typing import List

def floyd_warshall(graph: List[List[int]]) -> List[List[int]]:
    n = len(graph)

    # Copy graph so original matrix is not modified
    dist = [row[:] for row in graph]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    dist[i][j] = min(
                        dist[i][j],
                        dist[i][k] + dist[k][j]
                    )

    return dist


# Example graph
INF = float('inf')

graph = [
    [0,   5,  INF, 10],
    [INF, 0,   3,  INF],
    [INF, INF, 0,   1],
    [INF, INF, INF, 0]
]

result = floyd_warshall(graph)

for row in result:
    print(row)