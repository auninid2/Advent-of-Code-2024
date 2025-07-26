# ---------------------------------
# ------ Day 4: Ceres Search ------
# ---------------------------------

with open("inputs/day4_input.txt") as file:
    matrix = [list(line.strip()) for line in file]

n = len(matrix)
m = len(matrix[0])

def search_xmas(matrix):
    total = 0
    word = "XMAS"
    directions = [  
        (-1, 0),  # above
        (1, 0),   # below
        (0, -1),  # left
        (0, 1),   # right
        (-1, -1), # diagonal above left
        (-1, 1),  # diagonal above right
        (1, -1),  # diagonal below left
        (1, 1),   # diagonal below right
    ]

    for i in range(n):
        for j in range(m):
            for dx, dy in directions:
                try:
                    if all(
                        0 <= i + k*dx < n and 
                        0 <= j + k*dy < m and 
                        matrix[i + k*dx][j + k*dy] == word[k]
                        for k in range(len(word))
                    ):
                        total += 1
                except IndexError:
                    continue

    return total

def search_x_mas(matrix):
    total = 0

    def check_diagonal(line, col, dx1, dy1, dx2, dy2, pattern):
        try:
            return (
                matrix[line + dx1][col + dy1] == pattern[0] and
                matrix[line][col] == pattern[1] and
                matrix[line + dx2][col + dy2] == pattern[2]
            )
        except IndexError:
            return False

    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if matrix[i][j] != 'A':
                continue

            diag1_MAS = check_diagonal(i, j, -1, -1, 1, 1, "MAS")
            diag1_SAM = check_diagonal(i, j, -1, -1, 1, 1, "SAM")

            diag2_MAS = check_diagonal(i, j, -1, 1, 1, -1, "MAS")
            diag2_SAM = check_diagonal(i, j, -1, 1, 1, -1, "SAM")

            if (diag1_MAS or diag1_SAM) and (diag2_MAS or diag2_SAM):
                total += 1

    return total

print("XMAS appears a total of", search_xmas(matrix), "times")
print("X-MAS appears a total of", search_x_mas(matrix), "times")