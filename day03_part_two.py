import aoc


data = aoc.getLinesForDay(3, force_filepath="inputs/day03_example.txt")

num_digits = len(data[0])
num_to_remove = num_digits - 12

total = 0
for line in data:
    digits = [int(digit) for digit in line]
    removed = 0
    # 1. Remove digits preceding a greater value
    while ((less_than_next := [idx
                               for idx, digit in enumerate(digits[:-1])
                               if digit < digits[idx + 1]])
           and removed < num_to_remove):
        digits.pop(min(less_than_next))
        removed += 1
    # 2. Remove low value digits
    while removed < num_to_remove:
        digits.remove(min(digits))
        removed += 1
    total += int("".join(map(str, digits)))
print(total)
