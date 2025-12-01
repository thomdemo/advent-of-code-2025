import aoc


lines = aoc.getLinesForDay(1, force_filepath="inputs/day01_example.txt")

is_zero = 0
pos = 50
for line in lines:
    dir, num = line[0], int(line[1:])
    sign = 1 if dir == "R" else -1
    pos = (pos + sign * num) % 100
    if pos == 0:
        is_zero += 1
print(is_zero)
