import aoc


data = aoc.getLinesForDay(5, force_filepath="inputs/day05_example.txt")

ranges = [tuple(map(int, elt.split("-"))) for elt in data if "-" in elt]
numbers = [int(elt) for elt in data if elt != "" and "-" not in elt]

valid_numbers = set()
for num in numbers:
    for low, high in ranges:
        if low <= num <= high:
            valid_numbers.add(num)
print(len(valid_numbers))
