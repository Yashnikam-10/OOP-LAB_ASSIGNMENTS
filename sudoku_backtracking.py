def print_grid(arr):
    for i in range(9):
        for j in range(9):
            print(arr[i][j], end='  ')
        print()


def find_empty_slot(arr, slot):
    for i in range(9):
        for j in range(9):
            if arr[i][j] == 0:
                slot[0] = i
                slot[1] = j
                return True
    return False


def used_in_row(arr, row, num):
    for j in range(9):
        if arr[row][j] == num:
            return True
    return False


def used_in_column(arr, col, num):
    for i in range(9):
        if arr[i][col] == num:
            return True
    return False


def used_in_box(arr, row, col, num):
    for i in range(3):
        for j in range(3):
            if arr[i + row][j + col] == num:
                return True
    return False


def check_location_is_safe(arr, row, col, num):
    return (not used_in_row(arr, row, num) and
            not used_in_column(arr, col, num) and
            not used_in_box(arr, row - (row % 3), col - (col % 3), num))


def solve_sudoku(arr):
    slot = [0, 0]
    if not (find_empty_slot(arr, slot)):
        return True

    row = slot[0]
    col = slot[1]

    for num in range(1, 10):
        if check_location_is_safe(arr, row, col, num):
            arr[row][col] = num
            if solve_sudoku(arr):
                return True

            arr[row][col] = 0

    return False


# grid = [[0, 0, 0, 0, 0, 0, 0, 4, 2],
#         [0, 4, 5, 0, 8, 6, 1, 9, 0],
#         [3, 9, 8, 0, 0, 0, 0, 0, 6],
#         [4, 1, 0, 0, 0, 9, 0, 0, 0],
#         [0, 0, 6, 1, 0, 8, 7, 0, 0],
#         [0, 0, 0, 6, 0, 0, 0, 3, 1],
#         [6, 0, 0, 0, 0, 0, 2, 8, 7],
#         [0, 8, 3, 2, 1, 0, 9, 6, 0],
#         [9, 2, 0, 0, 0, 0, 0, 0, 0]]

grid = [[0 for i in range(9)] for j in range(9)]

for i in range(9):
    for j in range(9):
        grid[i][j] = int(input('Enter element of row {} and column {}: '.format(i+1, j+1)))

if solve_sudoku(grid):
    print_grid(grid)

else:
    print("No solution found...")
