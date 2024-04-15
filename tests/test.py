import random

rows, cols = (5, 5)
arr = [[0] * cols] * rows


# # print(arr)
#
# col_number = 0
# for i in range(0, 100, 20):
#     row_number = 0
#     for j in range(0, 100, 20):
#         print(f"i = {i}, j = {j}, row_counter = {row_number}, col_counter = {col_number}")
#         row_number += 1
#     col_number += 1
#
#
# for _ in range(10):
#     print(random.random())

def get_neighbors(matrix, row, col):
    neighbors = []
    rows = len(matrix)
    cols = len(matrix[0])

    # Define the range for neighboring cells
    row_range = range(max(0, row - 1), min(rows, row + 2))
    col_range = range(max(0, col - 1), min(cols, col + 2))

    # Iterate over neighboring cells
    for i in row_range:
        for j in col_range:
            if (i, j) != (row, col):
                neighbors.append(matrix[i][j])

    return neighbors


# Example usage
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

row_index = 1
col_index = 1
neighbors = get_neighbors(matrix, row_index, col_index)
print("Neighbors of cell ({}, {}):".format(row_index, col_index), neighbors)
