import numpy as np

input = [line.strip() for line in open('input')]

# input = [
# '00100',
# '11110',
# '10110',
# '10111',
# '10101',
# '01111',
# '00111',
# '11100',
# '10000',
# '11001',
# '00010',
# '01010',
# ]

# part 1
m = np.array([list(str) for str in input], dtype = int)
gamma = []
epsilon = []
nums = len(m)

for bit in range(len(m[0])):
    col = m[:,bit]
    if sum(col) > nums/2:
        gamma.append(1)
    else:
        gamma.append(0)

epsilon = [x^1 for x in gamma]

g = int(''.join([str(x) for x in gamma]), 2)
e = int(''.join([str(x) for x in epsilon]), 2)
print(g * e)

# part 2
m = np.array([list(str) for str in input], dtype = int)

def search(mem, b, type):
    if len(mem) == 1:
        return mem[0]

    if type == 'o':
        if sum(mem[:,b]) >= len(mem)/2:
            return search(mem[np.where(mem[:,b] == 1)], b+1, type)
        else:
            return search(mem[np.where(mem[:,b] == 0)], b+1, type)
    else:
        if sum(mem[:,b]) >= len(mem)/2:
            return search(mem[np.where(mem[:,b] == 0)], b+1, type)
        else:
            return search(mem[np.where(mem[:,b] == 1)], b+1, type)


o = int(''.join([str(x) for x in search(m, 0, 'o')]), 2)
c = int(''.join([str(x) for x in search(m, 0, 'c')]), 2)
print(o * c)