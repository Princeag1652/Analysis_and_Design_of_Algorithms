
import heapq


class ShortestPath:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.graph = [[] for _ in range(vertices)]

        # Store edges in adjacency-list form for Dijkstra
        for u, v, weight in edges:
            self.graph[u].append((v, weight))

    def dijkstra(self, src: int) -> list:
        if not 0 <= src < self.vertices:
            raise ValueError("Invalid source node")

        # Dijkstra does not support negative edge weights
        if any(weight < 0 for _, _, weight in self.edges):
            raise ValueError(
                "Dijkstra cannot handle negative edge weights"
            )

        dist = [float("inf")] * self.vertices
        dist[src] = 0

        # Priority queue stores (distance, node)
        pq = [(0, src)]

        while pq:
            current_dist, u = heapq.heappop(pq)

            # Ignore outdated queue entries
            if current_dist > dist[u]:
                continue

            for v, weight in self.graph[u]:
                new_dist = current_dist + weight

                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(pq, (new_dist, v))

        return dist

    def bellman_ford(self, src: int) -> list:
        if not 0 <= src < self.vertices:
            raise ValueError("Invalid source node")

        dist = [float("inf")] * self.vertices
        dist[src] = 0

        # Relax every edge at most V - 1 times
        for _ in range(self.vertices - 1):
            updated = False

            for u, v, weight in self.edges:
                if dist[u] != float("inf"):
                    new_dist = dist[u] + weight

                    if new_dist < dist[v]:
                        dist[v] = new_dist
                        updated = True

            # Stop early if no distance changes
            if not updated:
                break

        # Check for a reachable negative-weight cycle
        for u, v, weight in self.edges:
            if (dist[u] != float("inf")
                    and dist[u] + weight < dist[v]):
                return "Error: Negative-weight cycle detected"

        return dist


# ---------------- MAIN PROGRAM ----------------

if __name__ == "__main__":
    # Graph: (source, destination, weight)
    edges = [
        (0, 1, 4),
        (0, 2, 1),
        (2, 1, 2),
        (1, 3, 1),
        (2, 3, 5),
        (3, 4, 3)
    ]

    sp = ShortestPath(5, edges)

    print("Graph: 5 vertices (0 to 4)")
    print("Source node: 0")
    print("\nDijkstra's Algorithm:")
    print(sp.dijkstra(0))

    print("\nBellman-Ford Algorithm:")
    print(sp.bellman_ford(0))
