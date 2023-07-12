import re

data = "target area: x=253..280, y=-73..-46"
xmin, xmax, ymin, ymax = map(int, re.findall(r"-?\d+", data))


def steps_for_dy(dy):
    y = 0
    s = 0
    ss = []
    while y >= ymin:
        if ymin <= y <= ymax:
            ss.append(s)
        y += dy
        dy -= 1
        s += 1
    return ss


def dx_for_step(step):
    ss = set()
    for dx in range(1, xmax+1):
        s = dx
        x = 0
        for _ in range(step):
            x += dx
            if dx > 0:
                dx -= 1
            elif dx < 0:
                dx += 1
        if xmin <= x <= xmax:
            ss.add(s)
    return ss


dy = -ymin
ans1 = 0
ans2 = set()
while True:
    for steps in steps_for_dy(dy):
        dx_dy = dx_for_step(steps)
        if dx_dy and ans1 == 0:
            ans1 = sum(range(1, dy + 1))
        for dx in dx_dy:
            ans2.add((dx, dy))
    dy -= 1
    if dy < ymin:
        break

print("ans1", ans1)
print("ans2", len(ans2))
