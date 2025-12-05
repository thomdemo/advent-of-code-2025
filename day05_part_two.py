import aoc


data = aoc.getLinesForDay(5, force_filepath="inputs/day05_example.txt")
ranges = [tuple(map(int, elt.split("-"))) for elt in data if "-" in elt]

def is_overlap(range1, range2):
    return not (range1[1] < range2[0]  # r1 < r2
                or range1[0] > range2[1])  # r2 < r1

def merge(range1, range2):
    return (min(range1[0], range2[0]), max(range1[1], range2[1]))

def is_range1_in_range2(range1, range2):
    return (range2[0] <= range1[0] <= range2[1]
            and range2[0] <= range1[1] <= range2[1])

def get_no_overlap_arr(range, visited):
    return [not is_overlap(range, range_vis) for range_vis in visited]

to_process_queue = ranges.copy()
visited = []
while to_process_queue:
    range = to_process_queue.pop()

    if not visited:  # init
        visited.append(range)
    else:

        if all(get_no_overlap_arr(range, visited)):
            visited.append(range)
        else:

            while not all(is_no_overlap_li := get_no_overlap_arr(range, visited)):

                # Process the overlap case
                idx = is_no_overlap_li.index(False)
                range_vis = visited[idx]
                # Pop element in both case
                visited.pop(idx)
                if is_range1_in_range2(range, range_vis):
                    to_process_queue.append(range_vis)
                else:  # merge overlap
                    to_process_queue.append(merge(range, range_vis))

print(sum(high - low + 1 for low, high in visited))
