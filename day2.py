# ---------------------------------
# --- Day 2: Red-Nosed Reports ----
# ---------------------------------

# --- Part One----

from itertools import pairwise

def is_safe(digits):
    diffs = [b - a for a, b in pairwise(digits)]
    all_increasing = all(d > 0 for d in diffs)
    all_decreasing = all(d < 0 for d in diffs)
    all_in_range = all(1 <= abs(d) <= 3 for d in diffs)
    return (all_increasing or all_decreasing) and all_in_range

list1 = []

with open("inputs/day2_input.txt", "r") as file:
    for line in file:
        list1.append(line.strip())

safe_reports = 0

for line in list1:
    digits = [int(ch) for ch in line.split()]
    if is_safe(digits):
        safe_reports += 1

print("Number of safe reports:", safe_reports)

# --- Part Two ---

dampered_reports = 0

for line in list1:
    digits = [int(ch) for ch in line.split()]

    if is_safe(digits):
        dampered_reports += 1
        continue

    for i in range(len(digits)):
        test_digits = digits[:i] + digits[i+1:]
        if is_safe(test_digits):
            dampered_reports += 1
            break

print("Number of dampered reports:", dampered_reports)