# -------------------------------
# ----- Day 4: Ceres Search -----
# -------------------------------

with open("inputs/day4_input.txt") as file:
    matrix = [list(line.strip()) for line in file]

n = len(matrix)
m = len(matrix[0])

WORD_XMAS = "XMAS"
X_MAS_PATTERNS = ["MAS", "SAM"]

DIRECTIONS = [  
    (-1, 0),  # up
    (1, 0),   # down
    (0, -1),  # left
    (0, 1),   # right
    (-1, -1), # diag up-left
    (-1, 1),  # diag up-right
    (1, -1),  # diag down-left
    (1, 1),   # diag down-right
]

# --- Part One ---

def count_word_occurrences(matrix, word):
    count = 0
    word_len = len(word)

    for i in range(n):
        for j in range(m):
            for dx, dy in DIRECTIONS:
                if all(
                    0 <= i + k*dx < n and
                    0 <= j + k*dy < m and
                    matrix[i + k*dx][j + k*dy] == word[k]
                    for k in range(word_len)
                ):
                    count += 1
    return count

# --- Part Two ---

def count_x_mas_patterns(matrix):
    count = 0

    def match_diag(i, j, pattern, dx1, dy1, dx2, dy2):
        return (
            0 <= i + dx1 < n and 0 <= j + dy1 < m and
            0 <= i + dx2 < n and 0 <= j + dy2 < m and
            matrix[i + dx1][j + dy1] == pattern[0] and
            matrix[i][j] == pattern[1] and
            matrix[i + dx2][j + dy2] == pattern[2]
        )

    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if matrix[i][j] != 'A':
                continue

            diag1_matches = any(
                match_diag(i, j, pattern, -1, -1, 1, 1) for pattern in X_MAS_PATTERNS
            )
            diag2_matches = any(
                match_diag(i, j, pattern, -1, 1, 1, -1) for pattern in X_MAS_PATTERNS
            )

            if diag1_matches and diag2_matches:
                count += 1
    return count

print("XMAS appears a total of", count_word_occurrences(matrix, WORD_XMAS), "times")
print("X-MAS appears a total of", count_x_mas_patterns(matrix), "times")