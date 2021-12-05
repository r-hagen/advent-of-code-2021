input = [line.strip() for line in open('input')]

# input = [
# 'forward 5',
# 'down 5',
# 'forward 8',
# 'up 3',
# 'down 8',
# 'forward 2',
# ]

# part 1
h = 0
d = 0
for cmd in input:
    line = cmd.split()
    c = line[0]
    x = int(line[1])
    if (c == 'forward'):
        h += x
    elif (c == 'down'):
        d += x
    else:
        d -= x
print(h * d)


# part 2
a = 0
h = 0
d = 0
for cmd in input:
    line = cmd.split()
    c = line[0]
    x = int(line[1])
    if (c == 'forward'):
        h += x
        d += a * x
    elif (c == 'down'):
        a += x
    else:
        a -= x
print(h * d)