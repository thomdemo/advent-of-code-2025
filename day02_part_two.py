import aoc


data = aoc.getInputForDay(2, force_filepath="inputs/day02_example.txt")

reps = set()
for range_str in data.split(","):
    low, high = [int(elt) for elt in range_str.split("-")]
    for val in range(low, high + 1):
        val_str = str(val)
        for denom in range(2, len(val_str) + 1):
            batch_size = len(val_str) // denom
            batches = [val_str[start:start+batch_size] for start in range(0, len(val_str), batch_size)]
            if all(elt == batches[0] for elt in batches):
                reps.add((range_str, val))
print(sum(t[1] for t in reps))
