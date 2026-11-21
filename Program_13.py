from typing import List

class TSPSolver:

    def solve_tsp(self, dist_matrix: List[List[int]]) -> int:
        n = len(dist_matrix)

        if n == 0:
            return 0

        INF = float('inf')
        total_masks = 1 << n

        # dp[mask][i] = minimum cost to reach city i
        # after visiting cities represented by mask
        dp = [[INF] * n for _ in range(total_masks)]

        # Start from city 0
        dp[1][0] = 0

        # Iterate through all subsets of visited cities
        for mask in range(total_masks):
            for i in range(n):

                if dp[mask][i] == INF:
                    continue

                # Try visiting an unvisited city j
                for j in range(n):

                    if mask & (1 << j):
                        continue

                    new_mask = mask | (1 << j)

                    new_cost = dp[mask][i] + dist_matrix[i][j]

                    dp[new_mask][j] = min(
                        dp[new_mask][j],
                        new_cost
                    )

        # All cities visited
        full_mask = total_masks - 1

        # Return to starting city 0
        ans = INF

        for i in range(n):
            ans = min(ans, dp[full_mask][i] + dist_matrix[i][0])

        return int(ans) if ans != INF else -1


# Example usage
dist_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

solver = TSPSolver()
print(solver.solve_tsp(dist_matrix))