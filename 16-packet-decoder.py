pyint = int

def int(x, y = 10):
    return pyint("".join(x), y)

data = open("input", "r").readline()

k = list("".join(bin(int(c, 16))[2:].zfill(4) for c in data.strip()))
print(k)

def parse(k):
    version = int(k[:3], 2)
    k[:] = k[3:]
    typeid = int(k[:3], 2)
    k[:] = k[3:]
    if typeid == 4:
        data = []
        while True:
            cont = k.pop(0)
            data += k[:4]
            k[:] = k[4:]
            if cont == "0": break
        data = int(data, 2)
        return (version, typeid, data)
    else:
        packets = []
        if k.pop(0) == "0":
            length = int(k[:15], 2)
            k[:] = k[15:]
            d = k[:length]
            k[:] = k[length:]
            while d:
                packets.append(parse(d))
        else:
            num = int(k[:11], 2)
            k[:] = k[11:]
            for _ in range(num):
                packets.append(parse(k))
        return (version, typeid, packets)

def vsum(k):
    t = k[0]
    if k[1] == 4:
        return t
    else:
        return t + sum(map(vsum, k[2]))

q = parse(k)

print(vsum(q))


# part 2
def vsum2(k):
    if k[1] == 0:
        return sum(map(vsum2, k[2]))
    elif k[1] == 1:
        t = 1
        for q in k[2]:
            t *= vsum2(q)
        return t
    elif k[1] == 2:
        return min(map(vsum2, k[2]))
    elif k[1] == 3:
        return max(map(vsum2, k[2]))
    elif k[1] == 4:
        return k[2]
    elif k[1] == 5:
        return vsum2(k[2][0]) > vsum2(k[2][1])
    elif k[1] == 6:
        return vsum2(k[2][0]) < vsum2(k[2][1])
    elif k[1] == 7:
        return vsum2(k[2][0]) == vsum2(k[2][1])

print(vsum2(q))
