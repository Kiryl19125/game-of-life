import random

rows, cols = (5, 5)
arr = [[0]*cols]*rows
# print(arr)

col_number = 0
for i in range(0, 100, 20):
    row_number = 0
    for j in range(0, 100, 20):
        print(f"i = {i}, j = {j}, row_counter = {row_number}, col_counter = {col_number}")
        row_number += 1
    col_number += 1


for _ in range(10):
    print(random.random())
