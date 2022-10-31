example = """
2524255331
1135625881
2838353863
1662312365
6847835825
2185684367
6874212831
5387247811
2255482875
8528557131
"""

input = [list(map(int, list(line))) for line in example.strip().split("\n")]
# print(input)


def flash(grid, i, j, flashed = []):
    max_i = len(grid)-1
    max_j = len(grid[0])-1

    energy = grid[i][j]
    if energy <= 9: return

    if (i,j) in flashed: return
    else: flashed.append((i,j))

    if 0 <= i-1 <= max_i: 
        grid[i-1][j] += 1
        flash(grid, i-1, j, flashed)
    if 0 <= i+1 <= max_i: 
        grid[i+1][j] += 1
        flash(grid, i+1, j, flashed)
    if 0 <= j-1 <= max_j: 
        grid[i][j-1] += 1
        flash(grid, i, j-1, flashed)
    if 0 <= j+1 <= max_j: 
        grid[i][j+1] += 1
        flash(grid, i, j+1, flashed)
    if 0 <= i-1 <= max_i and 0 <= j-1 <= max_j: 
        grid[i-1][j-1] += 1
        flash(grid, i-1, j-1, flashed)
    if 0 <= i+1 <= max_i and 0 <= j+1 <= max_j: 
        grid[i+1][j+1] += 1
        flash(grid, i+1, j+1, flashed)
    if 0 <= i-1 <= max_i and 0 <= j+1 <= max_j: 
        grid[i-1][j+1] += 1
        flash(grid, i-1, j+1, flashed)
    if 0 <= i+1 <= max_i and 0 <= j-1 <= max_j: 
        grid[i+1][j-1] += 1
        flash(grid, i+1, j-1, flashed)


def step(grid):
    # increase energy level of each by 1
    grid = [list(map(lambda e: e+1, energies)) for energies in grid]
    flashed = []

    # flash all eq 9
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            energy_level = grid[i][j]
            if energy_level > 9:
                flash(grid, i, j, flashed)

    # set flashed ones to 0
    for (i,j) in flashed:
        grid[i][j] = 0

    # print(grid)
    # print(len(flashed))
    return (grid, flashed)


grid = input
print(grid)

flashes = 0
step_all = 0
i = 1
while step_all == 0:
    print(f"--- Step {i+1} ---")
    grid, flashed = step(grid)
    flashes += len(flashed)
    print(grid)
    print(flashes)

    all_flash = all([x == 0 for row in grid for x in row])
    if all_flash:
        step_all = i
        print(i)
    else: i += 1

