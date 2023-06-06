from typing import List, Tuple

def get_neighbours(matrix: List[List[int]], row: int, col: int) -> List[int]:
    neighbours = []
    print(f'--row={row}')
    print(f'--col={col}')
    print(f'--num_rows={len(matrix)}')
    print(f'--num_cols={len(matrix[0])}')
    num_rows = len(matrix)
    num_cols = len(matrix[row])
    if row == 0:
        if col == 0:
            neighbours.append(matrix[row][col+1])
            neighbours.append(matrix[row+1][col])
        elif col == num_cols-1:
            neighbours.append(matrix[row][num_cols-2])
            neighbours.append(matrix[row+1][num_cols-1])
        else:
            neighbours.append(matrix[row][col-1])
            neighbours.append(matrix[row][col+1])
            neighbours.append(matrix[row+1][col])
    elif row == num_rows-1:
        if col == 0:
            neighbours.append(matrix[row][col+1])
            neighbours.append(matrix[row-1][col])
        elif col == num_cols-1:
            neighbours.append(matrix[row][num_cols-2])
            neighbours.append(matrix[row+1][num_cols-1])
        else:
            neighbours.append(matrix[row][col-1])
            neighbours.append(matrix[row][col+1])
            neighbours.append(matrix[num_rows-2][col])
    elif col == 0:
        neighbours.append(matrix[row][col+1])
        neighbours.append(matrix[row-1][col])
        neighbours.append(matrix[row+1][col])
    elif col == num_cols-1:
        neighbours.append(matrix[row][col-2])
        neighbours.append(matrix[row-1][col])
        neighbours.append(matrix[row+1][col])
    else:
        neighbours.append(matrix[row-1][col])
        neighbours.append(matrix[row+1][col])
        neighbours.append(matrix[row][col+1])
        neighbours.append(matrix[row][col-1])
    return sorted(neighbours)

def read_input() -> Tuple[List[List[int]], int, int]:
    n = int(input())
    m = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().strip().split())))
    row = int(input())
    col = int(input())
    return matrix, row, col

matrix, row, col = read_input()
print(" ".join(map(str, get_neighbours(matrix, row, col))))
