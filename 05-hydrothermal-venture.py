def parseInput():
    points = []
    for line in open('input'):
        s1, s2 = line.split(' -> ')
        p1 = point(s1)
        p2 = point(s2)
        points.append([p1, p2])
    return points

def point(s: str):
    x,y = s.strip().split(',')
    return [int(x),int(y)]

def key(s1, s2):
    return str(s1)+','+str(s2)

point_pairs = parseInput()

# part 1
d1 = {}

for p1,p2 in point_pairs:
    x1, y1 = p1
    x2, y2 = p2
    if x1 == x2:
        #vertical
        start = min(y1,y2)
        end = max(y1,y2)
        for y in range(start,end+1):
            k = key(x1,y)
            d1[k] = d1.get(k, 0) + 1
    elif y1 == y2:
        #horizontal
        start = min(x1,x2)
        end = max(x1,x2)
        for x in range(start,end+1):
            k = key(x,y1)
            d1[k] = d1.get(k, 0) + 1

ans1 = sum([1 for x in d1.values() if x > 1])
print(ans1)

# part 2
d2 = {}

for p1,p2 in point_pairs:
    x1, y1 = p1
    x2, y2 = p2
    if x1 == x2:
        #vertical
        start = min(y1,y2)
        end = max(y1,y2)
        for y in range(start,end+1):
            k = key(x1,y)
            d2[k] = d2.get(k, 0) + 1
    elif y1 == y2:
        #horizontal
        start = min(x1,x2)
        end = max(x1,x2)
        for x in range(start,end+1):
            k = key(x,y1)
            d2[k] = d2.get(k, 0) + 1
    else:
        # diagonal
        xr = range(x1,x2+1) if x1 < x2 else range(x1,x2-1,-1)
        yr = range(y1,y2+1) if y1 < y2 else range(y1,y2-1,-1)
        for x,y in zip(xr,yr):
            k = key(x,y)
            d2[k] = d2.get(k, 0) + 1

ans2 = sum([1 for x in d2.values() if x > 1])
print(ans2)