
from dataclasses import dataclass
from typing import List
import heapq


@dataclass(frozen=True)
class Edge:
    u: int
    v: int
    weight: int

    def __str__(self):
        return f"({self.u}, {self.v}, weight={self.weight})"


class Graph:
    def __init__(self, vertices: int):
        self.V = vertices
        self.edges: List[Edge] = []
        self.adj = {i: [] for i in range(vertices)}

    def add_edge(self, u: int, v: int, weight: int):
        edge = Edge(u, v, weight)
        self.edges.append(edge)

        # Undirected graph
        self.adj[u].append((v, weight))
        self.adj[v].append((u, weight))

    # ---------- Kruskal's Algorithm ----------
    def kruskal_mst(self) -> List[Edge]:
        parent = list(range(self.V))
        rank = [0] * self.V

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if root_x == root_y:
                return False

            if rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            elif rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_y] = root_x
                rank[root_x] += 1

            return True

        mst = []

        # Process edges from smallest to largest weight
        for edge in sorted(self.edges, key=lambda e: e.weight):
            if union(edge.u, edge.v):
                mst.append(edge)

            if len(mst) == self.V - 1:
                break

        if len(mst) != self.V - 1:
            raise ValueError("Graph is disconnected; MST does not exist.")

        return mst

    # ---------- Prim's Algorithm ----------
    def prim_mst(self) -> List[Edge]:
        if self.V == 0:
            return []

        visited = set()
        mst = []
        min_heap = []
        counter = 0

        # Start from vertex 0
        visited.add(0)

        for v, weight in self.adj[0]:
            heapq.heappush(
                min_heap, (weight, counter, 0, v)
            )
            counter += 1

        while min_heap and len(visited) < self.V:
            weight, _, u, v = heapq.heappop(min_heap)

            if v in visited:
                continue

            # Select the minimum edge reaching a new vertex
            visited.add(v)
            mst.append(Edge(u, v, weight))

            for neighbor, w in self.adj[v]:
                if neighbor not in visited:
                    heapq.heappush(
                        min_heap,
                        (w, counter, v, neighbor)
                    )
                    counter += 1

        if len(visited) != self.V:
            raise ValueError("Graph is disconnected; MST does not exist.")

        return mst


# ---------- Example Usage ----------
if __name__ == "__main__":
    g = Graph(5)

    g.add_edge(0, 1, 2)
    g.add_edge(0, 3, 6)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 8)
    g.add_edge(1, 4, 5)
    g.add_edge(2, 4, 7)
    g.add_edge(3, 4, 9)

    print("Kruskal's MST:")
    kruskal_edges = g.kruskal_mst()
    for edge in kruskal_edges:
        print(edge)

    print("Total weight:",
          sum(edge.weight for edge in kruskal_edges))

    print("\nPrim's MST:")
    prim_edges = g.prim_mst()
    for edge in prim_edges:
        print(edge)

    print("Total weight:",
          sum(edge.weight for edge in prim_edges))
