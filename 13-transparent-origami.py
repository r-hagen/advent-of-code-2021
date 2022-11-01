data = open("input", "r").read()

dots = set()

t, b = data.split("\n\n")

for line in t.splitlines():
    x, y = map(int, line.split(","))
    dots.add((x, y))

# part 1
for line in b.splitlines():
    line = line[11:]
    f, n = line.split("=")
    n = int(n)
    if f == "x":
        dots = {(x if x < n else n - (x - n), y) for x, y in dots}
    else:
        dots = {(x, y if y < n else n - (y - n)) for x, y in dots}
    break

print(len(dots))


# part 2
for line in b.splitlines():
    line = line[11:]
    f, n = line.split("=")
    n = int(n)
    if f == "x":
        dots = {(x if x < n else n - (x - n), y) for x, y in dots}
    else:
        dots = {(x, y if y < n else n - (y - n)) for x, y in dots}

mx = min(x for x, y in dots)
my = min(y for x, y in dots)

dots = {(x - mx, y - my) for x, y in dots}

mx = max(x for x, y in dots)
my = max(y for x, y in dots)

g = [[" "] * (mx + 1) for _ in range(my + 1)]

for x, y in dots:
    g[y][x] = "#"

for r in g:
    print("".join(r))
