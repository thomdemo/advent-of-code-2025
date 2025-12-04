import aoc


grid = aoc.getCellsForDay(4, force_filepath="inputs/day04_example.txt")

def get_neighbors(grid, i, j):
    """8 neighbors."""
    n = len(grid)  # Square grid
    neighbors = []
    for ii, jj in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1),
                   (i + 1, j + 1), (i - 1, j + 1), (i + 1, j - 1), (i - 1, j - 1)]:
        if 0 <= ii < n and 0 <= jj < n:
            neighbors.append((ii, jj, grid[ii][jj]))
    return neighbors

total = 0
for row in range(n := len(grid)):
    for col in range(n):
        if grid[row][col] == "@":
            total += sum(cell[2] == "@" for cell in get_neighbors(grid, row, col)) < 4
print(total)
