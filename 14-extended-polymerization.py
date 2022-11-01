lines = open("input", "r").read().strip().split("\n")

# part 1
s = lines[0]

k = {}
for q in lines[2:]:
    x, y = q.split(" -> ")
    k[x] = y

for _ in range(10):
    n = s[0]
    for c in s[1:]:
        n += k[n[-1] + c]
        n += c
    s = n

c = {}
for char in s:
    if char not in c:
        c[char] = 0
    c[char] += 1

print(max(c.values()) - min(c.values()))

# part 2
s = lines[0]

pc = {}
for x, y in zip(s, s[1:]):
    if x + y not in pc:
        pc[x + y] = 0
    pc[x + y] += 1

k = {}
for q in lines[2:]:
    x, y = q.split(" -> ")
    k[x] = y

for _ in range(40):
    npc = {}
    for p in pc:
        q = k[p]

        if p[0] + q not in npc:
            npc[p[0] + q] = 0
        npc[p[0] + q] += pc[p]

        if q + p[1] not in npc:
            npc[q + p[1]] = 0
        npc[q + p[1]] += pc[p]
    pc = npc

hc = {}
tc = {}

for p in pc:
    if p[0] not in hc: hc[p[0]] = 0
    if p[1] not in tc: tc[p[1]] = 0
    hc[p[0]] += pc[p]
    tc[p[1]] += pc[p]

c = {x: max(hc.get(x, 0), tc.get(x, 0)) for x in set(hc) | set(tc)}

# for some reason 1 too much
print(max(c.values()) - min(c.values()))
