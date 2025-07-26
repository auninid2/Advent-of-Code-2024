# ---------------------------------
# ------ Day 3: Mull It Over ------
# ---------------------------------

import re

with open("inputs/day3_input.txt", "r") as file:
    content = file.read()

    # --- Part One ---
    total1 = sum(int(a) * int(b) for a, b in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", content))
    print("The result of all multiplications added up:", total1)

    # --- Part Two ---
    enabled = True
    total2 = 0

    pattern = re.finditer(r"(do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\))", content)
    for match in pattern:
        token = match.group(0)
        if token == "do()":
            enabled = True
        elif token == "don't()":
            enabled = False
        elif enabled:
            a, b = match.group(2), match.group(3)
            total2 += int(a) * int(b)

    print("The result of all enabled multiplications added up:", total2)