import aoc


data = aoc.getInputForDay(2, force_filepath="inputs/day02_example.txt")

reps = set()
for range_str in data.split(","):
    low, high = [int(elt) for elt in range_str.split("-")]
    for val in range(low, high + 1):
        val_str = str(val)
        # Count expanding substrings
        for idx in range(1, len(val_str) // 2 + 1):
            if val_str.count(val_str[:idx]) * idx == len(val_str):
                reps.add((range_str, val))
print(sum(t[1] for t in reps))
