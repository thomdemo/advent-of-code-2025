import math

import aoc


data = aoc.getLinesForDay(6, force_filepath="inputs/day06_example.txt")

data = [line.split() for line in data]
operators = data.pop()

# Transpose
data = [[int(subli[idx]) for subli in data] for idx in range(len(data[0]))]

print(sum(math.prod(col) if op == "*" else sum(col)
          for op, col in zip(operators, data)))
