from typing import List

def strassen_multiply(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    n = len(A)

    # Base case: 1 x 1 matrix
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    # Divide matrices into 4 submatrices
    mid = n // 2

    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    # Matrix addition
    def add(X, Y):
        return [
            [X[i][j] + Y[i][j] for j in range(len(X))]
            for i in range(len(X))
        ]

    # Matrix subtraction
    def subtract(X, Y):
        return [
            [X[i][j] - Y[i][j] for j in range(len(X))]
            for i in range(len(X))
        ]

    # Strassen's 7 multiplications
    M1 = strassen_multiply(add(A11, A22), add(B11, B22))
    M2 = strassen_multiply(add(A21, A22), B11)
    M3 = strassen_multiply(A11, subtract(B12, B22))
    M4 = strassen_multiply(A22, subtract(B21, B11))
    M5 = strassen_multiply(add(A11, A12), B22)
    M6 = strassen_multiply(subtract(A21, A11), add(B11, B12))
    M7 = strassen_multiply(subtract(A12, A22), add(B21, B22))

    # Calculate result submatrices
    C11 = add(subtract(add(M1, M4), M5), M7)
    C12 = add(M3, M5)
    C21 = add(M2, M4)
    C22 = add(subtract(add(M1, M3), M2), M6)

    # Combine submatrices
    result = []

    for i in range(mid):
        result.append(C11[i] + C12[i])

    for i in range(mid):
        result.append(C21[i] + C22[i])

    return result


# Example
A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

print(strassen_multiply(A, B))