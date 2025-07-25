# ---------------------------------
# --- Day 1: Historian Hysteria ---
# ---------------------------------

from collections import Counter

list1 = []
list2 = []

with open("input.txt", "r") as file:
    acc = 0

    for line in file:
        for word in line.split():
            if acc % 2 == 0:
                list1.append(int(word))
            else: 
                list2.append(int(word))
            acc += 1

list1.sort()
list2.sort()

# --- Part One ----
total_distance = sum(abs(a - b) for a, b in zip(list1, list2))

# --- Part Two ---
counter = Counter(list2)
similarity_score = sum(counter[x] * x for x in list1)

print("Total distance between both lists:", total_distance)
print("Similarity score beetwen both lists:", similarity_score)