from typing import List


class GraphBacktracker:

    def __init__(self, graph: List[List[int]]):
        self.graph = graph
        self.n = len(graph)
        self.colors = [0] * self.n

    def is_safe(self, vertex: int, color: int) -> bool:

        for i in range(self.n):
            if self.graph[vertex][i] == 1:
                if self.colors[i] == color:
                    return False

        return True

    def graph_coloring(self, m: int) -> List[int]:

        self.colors = [0] * self.n

        if m <= 0 and self.n > 0:
            return []

        def backtrack(vertex):

            # All vertices are colored
            if vertex == self.n:
                return True

            # Try all available colors
            for color in range(1, m + 1):

                if self.is_safe(vertex, color):

                    # Assign color
                    self.colors[vertex] = color

                    # Color next vertex
                    if backtrack(vertex + 1):
                        return True

                    # Backtrack
                    self.colors[vertex] = 0

            return False

        if backtrack(0):
            return self.colors.copy()

        return []


# Example
graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]

solver = GraphBacktracker(graph)

print(solver.graph_coloring(3))