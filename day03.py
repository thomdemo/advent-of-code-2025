import aoc


data = aoc.getLinesForDay(3, force_filepath="inputs/day03_example.txt")

total = 0
for line in data:
    maxi = 0
    for idx1, char1 in enumerate(line):
        for idx2, char2 in enumerate(line):
            if idx2 > idx1 and int(char1 + char2) > maxi:
                maxi = int(char1 + char2)
    total += maxi
print(total)
