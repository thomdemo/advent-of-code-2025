import math

import aoc


data = aoc.getInputForDay(6, force_filepath="inputs/day06_example.txt")
# No strip while parsing here
data = [l for l in data.strip("\n").split("\n")]

operators = data.pop()

total = 0
subtotal = []
num_cols = len(data[0])
# Scan columns from right to left
for idx in range(num_cols - 1, -1, -1):
    number_str = "".join(row[idx] for row in data).strip()
    if number_str != "":
        subtotal.append(int(number_str))
        if (op := operators[idx]) != " ":
            total += sum(subtotal) if op == "+" else math.prod(subtotal)
            subtotal = []

print(total)
