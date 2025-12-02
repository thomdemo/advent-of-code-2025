import aoc


data = aoc.getInputForDay(2, force_filepath="inputs/day02_example.txt")

acc = 0
for range_str in data.split(","):
    low, high = [int(elt) for elt in range_str.split("-")]
    for val in range(low, high + 1):
        val_str = str(val)
        mid = len(val_str) // 2
        if val_str[:mid] == val_str[mid:]:
            acc += val
print(acc)
