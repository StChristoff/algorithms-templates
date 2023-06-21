from typing import List

# def transpond(rows, cols, matrix):
#     for digit in line:

#         while idx < len(line):


# def read_input() -> Tuple[int, int, List[List[int]]]:
#     rows = int(input())
#     cols = int(input())
#     matrix = [[int(digit) for digit in input().strip().split()] for _ in range(rows)]
#     return rows, cols, matrix


def read_input() -> List[List[int]]:
    rows = int(input())
    cols = int(input())
    matrix = [[None] * rows] * cols
    for idx in range(rows):
        for count, digit in enumerate(input().strip().split()):
            matrix[count][idx] = int(digit)
    # [[matrix[idx][count] = int(digit) for count, digit in enumerate(input().strip().split())] for idx in range(rows)]
    return matrix

for row in read_input():
    print(*row)
